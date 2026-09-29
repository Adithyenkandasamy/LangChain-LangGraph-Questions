"""
PRACTICAL CHALLENGE: Preserving State Snapshots Across Iterations (LC-H6-P11)
=====================================================
ID: LC-H6-P11
Curriculum Tier: Advanced | Focus: LangGraph Loops & Document Crafter Agent
Task:
Implement a `StateCheckpointManager` that records a snapshot of the graph state at each iteration,
enabling history rollback and step debugging.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
import copy

class StateCheckpointManager:
    def __init__(self):
        self.checkpoints = []

    def save_checkpoint(self, step_name: str, state: dict):
        self.checkpoints.append({
            "step": step_name,
            "state": copy.deepcopy(state)
        })

    def get_step_state(self, step_idx: int) -> dict:
        return self.checkpoints[step_idx]["state"]

    def rollback_to_step(self, step_idx: int) -> dict:
        target = copy.deepcopy(self.checkpoints[step_idx]["state"])
        self.checkpoints = self.checkpoints[:step_idx + 1]
        return target

def test_checkpoints():
    mgr = StateCheckpointManager()
    state = {"count": 1}
    mgr.save_checkpoint("start", state)

    state["count"] = 2
    mgr.save_checkpoint("after_step1", state)

    state["count"] = 3
    mgr.save_checkpoint("after_step2", state)

    assert len(mgr.checkpoints) == 3
    rolled = mgr.rollback_to_step(1)
    assert rolled["count"] == 2
    assert len(mgr.checkpoints) == 2

if __name__ == '__main__':
    test_checkpoints()
    print("✓ Task 11 passed!")
