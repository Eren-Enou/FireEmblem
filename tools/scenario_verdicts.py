"""Narrow original-event assertions; never promotes full campaign acceptance."""
from tools.talk_evidence import CONVERSATION_KEY


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
