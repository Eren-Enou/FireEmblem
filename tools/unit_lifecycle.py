"""Stateful projections of pinned native force/escape paths (CAMP-016/017).

This is not a complete engine simulation. Linked-list ordering, rescue breakup,
map detach/refresh, native death, inventory workers and save I/O are unresolved.
Unknown paths raise before mutation. Retained payload is model-carried data,
not proof that transitive native calls preserve every byte.
"""
import copy
from tools.native_lifecycle import force_flags


class UnresolvedLifecycle(ValueError):
    pass


class Lifecycle:
    def __init__(self, units, *, shared=False):
        self.units = units if shared else copy.deepcopy(units)
        self.history = []
        self.unresolved = {'native refresh/map detach', 'linked-list order', 'save serialization'}
        self.validate()

    def validate(self):
        slots = []
        for key, unit in self.units.items():
            force_flags(unit['flags'], unit['force'])
            if unit.get('slot') is not None: slots.append(unit['slot'])
            if unit.get('pid', key) is None and unit['force'] != 4:
                raise ValueError('uninitialized record outside free pool')
        if len(slots) != len(set(slots)):
            raise ValueError('duplicate physical unit slot')

    def transfer(self, pid, destination):
        unit = self.units[pid]
        if unit.get('pid', pid) is None: raise ValueError('cannot transfer cleared identity')
        flags = force_flags(unit['flags'], destination)  # validate before write
        self.history.append(('transfer', pid, unit['force'], destination))
        unit['force'], unit['flags'] = destination, flags

    def return_owned(self, owners):
        # EXP-16's fixed PID table only, not force3 membership or draft bits.
        targets = []
        for pid, unit in self.units.items():
            identity = unit.get('pid', pid)
            if owners.get(identity) == 2 and unit['force'] == 3 and identity is not None:
                matches = [u for k, u in self.units.items() if u.get('pid', k) == identity]
                if len(matches) != 1: raise ValueError('ambiguous owned character identity')
                targets.append(pid)
        for pid in targets: self.transfer(pid, 0)

    def _preflight(self, pids):
        for pid in pids:
            unit = self.units[pid]
            if unit.get('pid', pid) is None: raise ValueError('cleared unit cannot escape')
            if unit['force'] not in (0, 1, 2, 3):
                raise UnresolvedLifecycle('escape outside active forces unsupported')
            if unit.get('rescue_link', 0):
                raise UnresolvedLifecycle('rescue breakup/native carried branches unresolved')

    def _worker(self, pid):
        unit = self.units[pid]
        if unit['force'] == 0:
            self.transfer(pid, 5)
            unit['flags'] |= 0x4000
            self.history.append(('escaped_to_roster', pid))
        else:
            # Directly pinned clearing stores, followed by append to free force4.
            previous = unit['force']
            unit.update(pid=None, force=4, flags=0, level=0, exp=0, hp=0, rescue_link=0)
            unit['inventory_slots_hex'] = None  # item-clear worker not modeled
            self.history.append(('uninitialized', pid, previous))
            self.unresolved.add('native item-clear worker')

    def escape(self, pid, *, owners=None):
        self._preflight([pid])
        if owners and owners.get(self.units[pid].get('pid', pid)) == 2 and self.units[pid]['force'] == 3:
            self.transfer(pid, 0)  # EXP-16 individual actor hand-back
        self._worker(pid)
        self.validate()

    def all_escape(self, *, owners=None):
        active = [pid for pid, u in self.units.items() if u['force'] in (0, 1, 2, 3)]
        self._preflight(active)  # reject carried paths before ownership/roster mutations
        if owners: self.return_owned(owners)
        for pid in [p for p in active if self.units[p]['force'] == 0]: self._worker(pid)
        for pid in active:
            if self.units[pid]['force'] in (0, 1, 2, 3): self._worker(pid)
        self.validate()

    def require_complete_native_proof(self):
        raise UnresolvedLifecycle('unresolved: ' + ', '.join(sorted(self.unresolved)))


def from_snapshot(snapshot):
    records = {}
    counts = {}
    for unit in snapshot['game']['units']:
        counts[unit['pid']] = counts.get(unit['pid'], 0) + 1
    for unit in snapshot['game']['units']:
        # Generic NPCs/enemies can legitimately share a character PID. Physical
        # slot is their distinct record identity; never silently collapse them.
        key = unit['pid'] if counts[unit['pid']] == 1 else f"{unit['pid']}#{unit['slot']}"
        if key in records: raise ValueError('duplicate snapshot record identity')
        records[key] = copy.deepcopy(unit)
    return Lifecycle(records)
