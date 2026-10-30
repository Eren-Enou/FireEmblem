"""Bounded original C07 battle-scene effects, never a battle/dispatch simulator."""
import copy
from tools.campaign_event_model import load_scripts,SCRIPT_SHA256
from tools.fe9.event_vm import execute

DISCOVERY='見つかるトリガ'


def discovery_scene(phase,flags,*,raw=None):
    """Execute original scene17; native actor/target facts are explicit tokens.

    This proves the scene's conditional/flag effect, not its engine activation.
    The caller may admit its observed effect only in the C06 combat probes.
    """
    if raw is None:raw=load_scripts()['Scripts/C07.cmb']
    values=dict(flags);bm={}
    def native(name,args):
        if name=='BMGetPhase' and not args:return phase
        if name=='MindGetMe' and not args:return 'actor'
        if name=='MindGetTarget' and not args:return 'target'
        if name=='BMSetValue' and len(args)==2 and args[0]==1:
            bm[1]=args[1];return 0
        if name=='set' and args==[DISCOVERY] and DISCOVERY in values:
            values[DISCOVERY]=True;return 0
        raise ValueError('unmodeled C07 battle-scene native: '+name)
    trace=execute(raw,17,native)
    return dict(values=values,bm=bm,trace=trace,
                script='Scripts/C07.cmb',script_sha256=SCRIPT_SHA256['Scripts/C07.cmb'],
                scene=17,scope='Original bytecode effect only; native scene dispatch and later discovery cutscene not established')


def event_effect(name,before,after,phase):
    """Admit only unchanged flags or the original C07 discovery flag effect."""
    if before==after:return True,None
    if name not in ('CH6-YELLOW-COMBAT','CH6-YELLOW-FATAL'):return False,None
    if not before.get('complete_table_read') or DISCOVERY not in before.get('values',{}):return False,None
    model=discovery_scene(phase,before['values'])
    expected=copy.deepcopy(before);expected['values']=model['values']
    if expected!=after:return False,None
    return True,dict(script=model['script'],script_sha256=model['script_sha256'],scene=model['scene'],
                     flag=DISCOVERY,before=before['values'][DISCOVERY],after=True,
                     scope=model['scope'])
