"""Narrow original-event assertions; never promotes full campaign acceptance."""
from tools.talk_evidence import CONVERSATION_KEY


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
