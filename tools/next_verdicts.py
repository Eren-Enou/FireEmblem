"""Strict local acceptance for new owner captures; no runtime automation."""
from tools.next_scenarios import BLUE,YELLOW,OBS7,OBS10
from tools.campaign_event_model import ESCAPE_KEYS,DOOR_KEYS
from tools.talk_evidence import CONVERSATION_KEY


def unit(game,pid,failures,label):
    matches=[u for u in game['units'] if u['pid']==pid]
    if len(matches)!=1:
        failures.append(label+': exactly one '+pid+' required');return None
    return matches[0]


def common(snaps,chapter_by_label,fingerprint,failures):
    hashes=[]
    for label,chapter in chapter_by_label.items():
        s=snaps[label];e=s['evidence'];g=s['game'];script=g.get('event_scripts',{})
        if not e.get('intended_c2_verified') or e.get('codes_fingerprint')!=fingerprint:
            failures.append(label+': wrong or unverified live codes')
        if g['chapter']!=chapter or not script.get('complete_chain') or script.get('campaign_ids')!=[chapter] or not script.get('chapter_matches'):
            failures.append(label+': original loaded chapter/script required')
        if not g.get('event_flags',{}).get('complete_table_read'):
            failures.append(label+': complete flag table required')
        hashes.append(e.get('state_sha256'))
    if not all(hashes) or len(set(hashes))!=len(hashes):failures.append('distinct captured states required')


def result(failures,observed,required,scope,**extras):
    failures+=['operator reported failed check: '+k for k in required if observed.get(k) is False]
    missing=[k for k in required if observed.get(k) is not True]
    return dict(status='FAIL' if failures else 'INCONCLUSIVE' if missing or extras.get('private_card_write_verified') is False else 'PASS',
                failures=failures,missing_observations=missing,scope=scope,
                excludes=['natural campaign history','internet Netplay','other chapters or event branches'],**extras)


def ch7_wait(snaps,observed,source):
    failures=[]
    common(snaps,dict(before=8,after=8),'8609ae9f49fd879f',failures)
    actors=[]
    for label in ('before','after'):
        g=snaps[label]['game']
        if (g['phase'],g['turn'])!=(3,1) or g['control'][3]!=1:
            failures.append(label+': original Yellow turn1/human control required')
        u=unit(g,'PID_OSCAR',failures,label);actors.append(u)
        if u and (u['force']!=3 or u['hp']<=0 or u['death_record'] or u['rescue_link']):
            failures.append(label+': living unrescued Yellow Oscar required')
    original=unit(source,'PID_OSCAR',failures,'accepted native source')
    if all(actors) and original:
        a,b=actors
        if a['flags']&1 or b['flags']!=a['flags']|1:failures.append('Oscar must acquire only acted bit')
        for u in actors:
            for key in ('slot','pid','class','hp','level','exp','inventory_slots_hex'):
                if u[key]!=original[key]:failures.append('native battle changed Oscar identity/progression/items: '+key)
        expected=[dict(u) for u in snaps['before']['game']['units']]
        next(u for u in expected if u['pid']=='PID_OSCAR')['flags']=b['flags']
        if expected!=snaps['after']['game']['units']:failures.append('Wait changed additional roster fields')
        for key in ('event_flags','event_scripts'):
            if snaps['before']['game'][key]!=snaps['after']['game'][key]:failures.append('Wait changed '+key)
    return result(failures,observed,OBS7,'Chapter7 original battle initialization after native Load; P2 Oscar Wait/P1 lockout on same Yellow turn')


def ch10_completion(snaps,observed,source,setup,card_write_verified=False):
    failures=[]
    common(snaps,dict(staged=11,before=11,after=11,next_prep=12,reloaded=12),'92f0ad0562beaef9',failures)
    staged,before=snaps['staged']['game'],snaps['before']['game']
    if (staged['phase'],staged['turn'])!=(3,1) or (before['phase'],before['turn'])!=(0,2):
        failures.append('staged Yellow1 -> original Blue2 queue required')
    if staged['control'][3]!=1 or before['control'][0]!=1:failures.append('human phase controls required')
    expected=[dict(u) for u in source['units']]
    for row in setup['records']:
        u=next(u for u in expected if u['slot']==row['slot'])
        u['xy']=list(row['destination_xy'])
    if staged['units']!=expected:failures.append('staging changed more than declared original positions')
    if staged['event_flags']!=source['event_flags']:failures.append('staging changed original flags')
    for pid in (*BLUE,*YELLOW,'PID_KEVIN','PID_MORDY'):
        initial=unit(source,pid,failures,'source')
        for label in snaps:
            u=unit(snaps[label]['game'],pid,failures,label)
            if not initial or not u:continue
            if u['hp']<=0 or u['death_record'] or u['rescue_link']:failures.append(label+': lost/dead/carried survivor '+pid)
            for key in ('pid','class','hp','level','exp','inventory_slots_hex','owned','owner'):
                if u[key]!=initial[key]:failures.append(label+': identity/progression/items changed '+pid+'/'+key)
            if label in ('next_prep','reloaded'):
                allowed=(0,5,7) if pid in ('PID_CHINON','PID_GATRIE','PID_VOKE') else (0,5)
                if u['force'] not in allowed:failures.append(label+': survivor not permanent/expected away '+pid)
            elif label=='before':
                force=0 if pid=='PID_IKE' else 5 if pid in BLUE or pid in ('PID_KEVIN','PID_MORDY') else 3
                if u['force']!=force:failures.append('before: incorrect Escape order/ownership '+pid)
                if pid in BLUE and pid!='PID_IKE' and not u['escaped']:failures.append('Blue queue did not genuinely escape '+pid)
                if pid=='PID_KEVIN' and not u['escaped']:failures.append('accepted Kieran original Escape marker lost')
            elif label=='after' and u['force'] not in (0,5,7):
                failures.append('after: original ending did not restore/retain '+pid)
    ike=unit(before,'PID_IKE',failures,'before')
    if ike and (ike['xy']!=[6,2] or ike['flags']&1):failures.append('Ike must be unacted at original exit LAST BLUE')
    for label in ('staged','before'):
        flags=snaps[label]['game']['event_flags']['values']
        if not flags.get(CONVERSATION_KEY) or not flags.get(ESCAPE_KEYS['PID_KEVIN']) or flags.get('gf_complete'):
            failures.append(label+': accepted Kieran history/unfinished chapter required')
        for pid in ('PID_CHAP','PID_NEPENEE'):
            if flags.get(DOOR_KEYS[pid]) or flags.get(ESCAPE_KEYS[pid]):failures.append(label+': unexpected prisoner history '+pid)
            u=unit(snaps[label]['game'],pid,failures,label)
            if u and u['force']!=2:failures.append(label+': unmet prisoner must still be Green '+pid)
    if not snaps['after']['game']['event_flags']['values'].get('gf_complete'):
        failures.append('original completion flag absent in ending capture')
    for label in ('next_prep','reloaded'):
        pids=[u['pid'] for u in snaps[label]['game']['units'] if u['force'] in (0,3,5,7)]
        if len(pids)!=len(set(pids)):failures.append(label+': duplicate permanent/away PID')
        for pid in ('PID_CHAP','PID_NEPENEE'):
            matches=[u for u in snaps[label]['game']['units'] if u['pid']==pid and u['force'] in (0,3,5)]
            if matches:failures.append(label+': prisoner retained despite unmet conditions '+pid)
    # Native loading can rebuild enemy slots. Compare permanent/away records by
    # PID, including all inventory bytes, but not their physical slot allocation.
    def retained(game):
        return sorted(({k:v for k,v in u.items() if k!='slot'} for u in game['units'] if u['force'] in (0,3,5,7)),key=lambda u:u['pid'])
    if retained(snaps['next_prep']['game'])!=retained(snaps['reloaded']['game']):
        failures.append('native reload changed complete permanent/away records')
    return result(failures,observed,OBS10,'synthetic C11 original ending, Kieran retention, C12 roster and standalone native save/fresh Load',
                  private_card_write_verified=card_write_verified,
                  story_limits='Inherited Shinon/Gatrie and optional Volke may be away. This does not validate their natural recruitment/departure history.')
