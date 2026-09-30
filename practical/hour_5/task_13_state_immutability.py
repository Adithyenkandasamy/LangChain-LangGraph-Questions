"""
PRACTICAL CHALLENGE: Safe State Immutability across Nodes (LC-H5-P13)
=====================================================
ID: LC-H5-P13
Curriculum Tier: Advanced | Focus: Tool Calling & LangGraph Basics
Task:
Implement node wrappers that verify input state is not mutated in-place and state updates
are returned as new dictionaries.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
import copy

def safe_node_runner(node_fn, current_state: dict) -> dict:
    state_snapshot = copy.deepcopy(current_state)
    updates = node_fn(copy.deepcopy(current_state))
    # verify current_state was not modified
    if current_state != state_snapshot:
        raise RuntimeError("Node improperly modified state in-place!")
    
    new_state = dict(current_state)
    new_state.update(updates)
    return new_state

def well_behaved_node(state):
    return {"count": state.get("count", 0) + 1}

def test_safe_state_runner():
    initial = {"count": 10, "label": "demo"}
    updated = safe_node_runner(well_behaved_node, initial)
    assert updated["count"] == 11
    assert initial["count"] == 10

if __name__ == '__main__':
    test_safe_state_runner()
    print("✓ Task 13 passed!")
