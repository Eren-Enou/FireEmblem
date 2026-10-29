"""Local original-action assertions. No battle simulator or campaign verdict."""
from tools.action_scenarios import SPECS
from tools.next_verdicts import common,result,unit
from tools.inspect_state import UNITS


def verify(name,snaps,observed,source,setup,fingerprint):
    failures=[];spec=SPECS[name];chapter=source['chapter']
    common(snaps,dict(before=chapter,after=chapter),fingerprint,failures)
    games={k:snaps[k]['game'] for k in ('before','after')}
    for label,g in games.items():
        if (g['phase'],g['turn'],g['control'][3])!=(3,1,1):failures.append(label+': same original human Yellow turn required')
        if g['event_flags']!=source['event_flags']:failures.append(label+': original event flags changed')
    before,after=games['before'],games['after']
    expected=[dict(u) for u in source['units']]
    for row in setup['records']:
        next(u for u in expected if u['slot']==row['slot'])['xy']=list(row['destination_xy'])
    if before['units']!=expected:failures.append('before differs from declared position-only setup')
    a=unit(before,spec['actor'],failures,'before');b=unit(after,spec['actor'],failures,'after')
    target=next((u for u in before['units'] if u['slot']==spec['target_slot']),None)
    other=[u for u in after['units'] if u['slot']==spec['target_slot']]
    if not a or not b or not target:return result(failures,observed,spec['observations'],'incomplete original action records')
    kind=spec['kind']
    for key in ('slot','pid','class','force','owned','owner'):
        if b[key]!=a[key] and not (kind=='fatal' and key=='force'):failures.append('actor identity/ownership changed: '+key)
    if a['force']!=3 or a['hp']<=0 or a['flags']&1 or a['rescue_link']:failures.append('available living Yellow actor required')
    if kind=='rescue':
        if len(other)!=1:failures.append('passenger missing or duplicated')
        else:
            passenger=other[0]
            ap=UNITS+(a['slot']-1)*0x280;tp=UNITS+(target['slot']-1)*0x280
            if b['rescue_link']!=tp or passenger['rescue_link']!=ap:failures.append('complete reciprocal rescue links required')
            if not b['flags']&2 or not passenger['flags']&4:failures.append('original carrier/passenger role bits required')
            if passenger['xy']!=b['xy']:failures.append('original Rescue must place passenger at carrier coordinates')
            for key in ('slot','pid','class','force','hp','level','exp','inventory_slots_hex','owned','owner','death_record','death_chapter'):
                if passenger[key]!=target[key]:failures.append('Rescue changed passenger '+key)
                if b[key]!=a[key]:failures.append('Rescue changed carrier '+key)
            if target['rescue_link'] or target['force']!=0:failures.append('initial Blue unrescued passenger required')
    elif kind=='fatal':
        if b['hp']!=0 or not b['death_record'] or b['death_chapter']!=chapter:
            # A surviving forecast probe is useful evidence, but cannot pass a
            # death test. Never loop combats or synthesize HP to force it.
            return dict(status='INCONCLUSIVE' if not failures else 'FAIL',failures=failures,
                        reason='Original one-attack fatal transition not demonstrated; preserve forecast/result.',
                        scope='fatal combat probe; persistent death/roster unavailable')
        if b['force'] not in (3,6):failures.append('unexpected original death force')
        for key in ('level','exp','rescue_link'):
            if b[key]!=a[key]:failures.append('fatal action changed '+key)
    else:
        if b['hp']<=0 or b['death_record'] or b['rescue_link']:failures.append('ordinary combat actor must survive')
        if other and (other[0]['pid']!=target['pid'] or other[0]['hp']>=target['hp']):failures.append('target damage/death absent')
        if len(other)>1:failures.append('duplicate target slot')
        if kind=='combat':
            if b['level']*100+b['exp']<=a['level']*100+a['exp']:failures.append('original combat EXP gain absent')
            old=bytes.fromhex(a['inventory_slots_hex']);new=bytes.fromhex(b['inventory_slots_hex'])
            # Source Oscar uses his original nonempty first Iron Lance. Its uses
            # byte is pinned via inventory accessor -> original decrement call.
            if len(old)!=64 or len(new)!=64 or new[:4]!=old[:4] or not 0<new[4]<old[4]:failures.append('original weapon uses decrement absent')
            if new[8:]!=old[8:]:failures.append('unrelated inventory slots changed')
        else:
            if b['owned'] or b['owner'] is not None or b['force']!=3:failures.append('native partner became persistently owned')
            if b['class']!='JID_CAT/F':failures.append('expected original transformed Lethe')
    changed={a['slot'],target['slot']}
    if [u for u in before['units'] if u['slot'] not in changed]!=[u for u in after['units'] if u['slot'] not in changed]:
        failures.append('unrelated roster changed during one action')
    scope={'rescue':'original Yellow Oscar Rescue of Blue Rhys; reciprocal identities only, no carried Escape',
           'combat':'original Yellow Oscar attack, damage, EXP and weapon uses; level-up not required/proven',
           'fatal':'original Yellow Oscar fatal combat and local persistent death record; later roster/cleanup NOT TESTED',
           'partner':'original transformed native Yellow Lethe combat; gauge/EXP measured, cleanup/recruitment NOT TESTED'}[kind]
    return result(failures,observed,spec['observations'],scope,
                  actor_changes={k:[a[k],b[k]] for k in a if a[k]!=b[k]})
