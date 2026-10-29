"""Narrow original-event assertions; never promotes full campaign acceptance."""
from tools.talk_evidence import CONVERSATION_KEY


def ch6_completion(snapshots, observed, card_write_verified=False):
    """Synthetic original Escape queue -> Ch7 prep -> human fresh native Load."""
    labels=('before_queue','before','after','next_prep','reloaded')
    missing=[label for label in labels if label not in snapshots]
    if missing:return {'status':'INCONCLUSIVE','failures':[],'missing_captures':missing}
    failures=[]
    survivors=('PID_IKE','PID_OSCAR','PID_TIAMAT','PID_KILROY','PID_SENERIO')
    records={}
    for label in labels:
        snap=snapshots[label];game,evidence=snap['game'],snap['evidence']
        chapter,turn=(7,2) if label in labels[:3] else (8,1)
        if not evidence.get('intended_c2_verified') or evidence.get('codes_fingerprint')!='e60e83a81d994e3b':
            failures.append(label+': original isolated Escape-queue codes required')
        if (game['chapter'],game['phase'],game['turn'])!=(chapter,0,turn) or game['control'][0]!=1:
            failures.append(label+': unexpected original chapter/turn/control')
        scripts=game.get('event_scripts',{})
        if not scripts.get('complete_chain') or scripts.get('campaign_ids')!=[chapter] or not scripts.get('chapter_matches'):
            failures.append(label+': original loaded chapter script required')
        if not game.get('event_flags',{}).get('complete_table_read'):
            failures.append(label+': registered flag table unverified')
        records[label]={}
        for pid in survivors:
            matches=[u for u in game['units'] if u['pid']==pid]
            if len(matches)!=1:failures.append(label+': exactly one '+pid+' required')
            else:
                unit=matches[0];records[label][pid]=unit
                if unit['hp']<=0 or unit['death_record'] or unit['rescue_link']:
                    failures.append(label+': survivor not living/unrescued: '+pid)
                expected=5 if label=='after' or (label=='before' and pid!='PID_IKE') or (label=='before_queue' and pid=='PID_OSCAR') else 0
                if unit['force']!=expected or (expected==5 and not unit['escaped']):
                    failures.append(label+': incorrect escape/preparation state: '+pid)
    if all(len(row)==len(survivors) for row in records.values()):
        ike=records['before']['PID_IKE']
        if ike['xy']!=[13,26] or ike['flags']&1:failures.append('Ike must be unacted at original exit before final Escape')
        for pid in survivors:
            initial=records['before_queue'][pid]
            for label in labels[1:]:
                unit=records[label][pid]
                for field in ('slot','pid','class','hp','level','exp'):
                    if unit[field]!=initial[field]:failures.append(label+': survivor progression/identity changed: '+pid+'/'+field)
            if records['next_prep'][pid]!=records['reloaded'][pid]:
                failures.append('native reload changed complete survivor record: '+pid)
        inventory=records['before_queue']['PID_OSCAR']['inventory_slots_hex']
        if any(records[label]['PID_OSCAR']['inventory_slots_hex']!=inventory for label in labels):
            failures.append('Oscar inventory changed across escape/transition/save/load')
    for pid in ('PID_CHINON','PID_GATRIE'):
        a=[u for u in snapshots['next_prep']['game']['units'] if u['pid']==pid]
        b=[u for u in snapshots['reloaded']['game']['units'] if u['pid']==pid]
        if len(a)!=1 or a!=b or a[0]['force']!=7:failures.append('native reload changed away record: '+pid)
    hashes=[snapshots[label]['evidence'].get('state_sha256') for label in labels]
    if not all(hashes) or len(set(hashes))!=len(labels):failures.append('five distinct captured states required')
    failures+=['human reported failed check: '+key for key,value in observed.items() if value is False]
    required=('remaining_blue_original_escapes','ike_last','original_completion','oscar_present_next_chapter','fresh_native_load')
    return {'status':'FAIL' if failures else 'PASS' if card_write_verified and all(observed.get(key) is True for key in required) else 'INCONCLUSIVE',
            'failures':failures,'private_card_write_verified':card_write_verified,
            'scope':'synthetic Ch6 original Escape queue/Ike-last, Ch7 survivor retention and standalone native save/fresh Load',
            'excludes':['naturally progressed campaign','Ch7 Player2 battle control','enemy slot reconstruction/whole-engine equivalence','carried escape','Netplay persistence']}


def native_resume(before, after, observed, card_write_verified=False):
    """Selected living-unit persistence plus explicit human fresh native load.

    Whole-engine serialization, enemy transient flags and natural campaign save
    histories are outside this verdict. Card changes alone never prove reload.
    """
    failures=[]
    for label,snap in (('before',before),('after',after)):
        game,evidence=snap['game'],snap['evidence']
        if not evidence.get('intended_c2_verified') or evidence.get('codes_fingerprint')!='c11089d39a0fe037':
            failures.append(label+': expected isolated post-Talk live configuration')
        if (game['chapter'],game['phase'],game['turn'])!=(11,3,1) or game['control'][3]!=1:
            failures.append(label+': expected Chapter10 turn1 human Yellow')
        scripts=game.get('event_scripts',{})
        if not scripts.get('complete_chain') or scripts.get('campaign_ids')!=[11] or not scripts.get('chapter_matches'):
            failures.append(label+': original loaded C11 required')
        if game.get('talk_fixture',{}).get('flags',{}).get(CONVERSATION_KEY) is not True:
            failures.append(label+': original consumed Talk key required')
        if not game.get('event_flags',{}).get('complete_table_read'):
            failures.append(label+': registered event flag table unverified')
    if before['evidence'].get('dolphin') != after['evidence'].get('dolphin'):
        failures.append('emulator versions differ')
    hashes=[s['evidence'].get('state_sha256') for s in (before,after)]
    if not all(hashes) or hashes[0]==hashes[1]:failures.append('distinct before/resumed states required')
    for key in ('control','event_flags'):
        if before['game'].get(key)!=after['game'].get(key):failures.append('changed '+key)
    for key in ('flags','cell_door','map_dimensions','cells'):
        if before['game'].get('talk_fixture',{}).get(key)!=after['game'].get('talk_fixture',{}).get(key):
            failures.append('changed local story/map state: '+key)
    for pid in ('PID_OSCAR','PID_KEVIN'):
        a=[u for u in before['game']['units'] if u['pid']==pid]
        b=[u for u in after['game']['units'] if u['pid']==pid]
        if len(a)!=1 or len(b)!=1 or a!=b:
            failures.append(pid+': complete selected record must persist')
        elif a[0]['force']!=3 or a[0]['hp']<=0 or a[0].get('death_record') or a[0].get('rescue_link'):
            failures.append(pid+': expected living unrescued Yellow')
    identities=lambda snap:sorted((u['slot'],u['pid']) for u in snap['game']['units'])
    if identities(before)!=identities(after):failures.append('roster identities changed')
    failures+=['human reported failed check: '+key for key,value in observed.items() if value is False]
    required=('native_suspend_accepted','fresh_boot_without_state','native_resume_selected',
              'same_roster_and_progression','no_unexpected_behavior')
    complete=card_write_verified and all(observed.get(key) is True for key in required)
    return {'status':'FAIL' if failures else 'PASS' if complete else 'INCONCLUSIVE',
            'failures':failures,'private_card_write_verified':card_write_verified,
            'scope':'original standalone Suspend and fresh native Resume; living Oscar/Kieran records and roster identities only',
            'excludes':['complete serialized engine state','enemy transient flag interpretation',
                        'permanent recruitment','chapter transition save','natural campaign history','Netplay persistence']}


def prisoner_escape(before, after, observed):
    failures = []
    for label, snap in (('before',before),('after',after)):
        game, evidence = snap['game'],snap['evidence']
        if not evidence.get('intended_c2_verified') or {n.split()[0] for n in evidence.get('codes',[])} != {'COOP-P6','EXP-16','FIXTURE-LOADER','DBG-CAMP-EXIT'}:
            failures.append(label+': expected isolated live Escape setup')
        if evidence.get('codes_fingerprint') != 'efc52ab6c1471602':
            failures.append(label+': expected prepared Escape configuration fingerprint')
        if (game['chapter'],game['phase'],game['turn']) != (11,3,1) or game['control'][3]!=1:
            failures.append(label+': expected original turn1 Yellow Chapter10')
        scripts=game.get('event_scripts',{})
        if not scripts.get('complete_chain') or scripts.get('campaign_ids')!=[11] or not scripts.get('chapter_matches'):
            failures.append(label+': original loaded C11 required')
        if game.get('talk_fixture',{}).get('flags',{}).get(CONVERSATION_KEY) is not True:
            failures.append(label+': original Talk outcome lost')
    if before['evidence'].get('codes_fingerprint') != after['evidence'].get('codes_fingerprint'):
        failures.append('configuration changed')
    hashes=[snap['evidence'].get('state_sha256') for snap in (before,after)]
    if not all(hashes) or hashes[0]==hashes[1]: failures.append('distinct captures required')
    units=[]
    for label,snap in (('before',before),('after',after)):
        matching=[u for u in snap['game']['units'] if u['pid']=='PID_KEVIN']
        if len(matching)!=1:
            failures.append(label+': exactly one original Kieran required')
        else: units.append(matching[0])
    if len(units)==2:
        a,b=units
        if a['force']!=3 or a['xy']!=[6,2] or a['flags']&1 or a['rescue_link'] or a['hp']<=0:
            failures.append('before Kieran must be living unacted Yellow at original exit')
        if b['force']!=5 or not b['escaped'] or b['death_record'] or b['rescue_link']:
            failures.append('after original player Escape must retain living Kieran in escaped roster')
        for field in ('slot','pid','class','hp','level','exp','inventory_slots_hex'):
            if a.get(field)!=b.get(field): failures.append('Kieran identity/progression changed: '+field)
    for pid in ('PID_OSCAR','PID_IKE'):
        a=[u for u in before['game']['units'] if u['pid']==pid]
        b=[u for u in after['game']['units'] if u['pid']==pid]
        if len(a)!=1 or a!=b: failures.append(pid+': unexpected change during Kieran Escape')
    failures += ['human reported failed check: '+k for k,v in observed.items() if v is False]
    required=('original_escape','p2_command','no_unexpected_behavior')
    return {'status':'FAIL' if failures else 'PASS' if all(observed.get(k) is True for k in required) else 'INCONCLUSIVE',
            'failures':failures,'scope':'synthetic local original Kieran Escape only',
            'excludes':['permanent recruitment','chapter cleanup/completion','native save/reload','natural campaign','Netplay']}
