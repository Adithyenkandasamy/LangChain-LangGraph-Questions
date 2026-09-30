"""
PRACTICAL CHALLENGE: LangGraph State Snapshot Inspector (LC-H7-P12)
=====================================================
ID: LC-H7-P12
Curriculum Tier: Mastery | Focus: Autonomous LangGraph RAG Agent
Task:
Implement `StateSnapshotManager` that logs state snapshots at each node execution
and provides a method `get_snapshot(step_index)` and `diff(idx1, idx2)`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
import copy

class StateSnapshotManager:
    def __init__(self):
        self.snapshots = []

    def record_step(self, node_name: str, state: dict):
        self.snapshots.append({
            "step": len(self.snapshots),
            "node": node_name,
            "state": copy.deepcopy(state)
        })

    def get_snapshot(self, idx: int) -> dict:
        return self.snapshots[idx]

    def diff_keys(self, idx1: int, idx2: int) -> list:
        s1 = self.snapshots[idx1]["state"]
        s2 = self.snapshots[idx2]["state"]
        changed = []
        for k in set(s1.keys()).union(s2.keys()):
            if s1.get(k) != s2.get(k):
                changed.append(k)
        return changed

def test_snapshots():
    sm = StateSnapshotManager()
    sm.record_step("start", {"step": 0, "status": "init"})
    sm.record_step("agent", {"step": 1, "status": "working"})
    assert len(sm.snapshots) == 2
    diff = sm.diff_keys(0, 1)
    assert "step" in diff and "status" in diff

if __name__ == '__main__':
    test_snapshots()
    print("✓ Task 12 passed!")
