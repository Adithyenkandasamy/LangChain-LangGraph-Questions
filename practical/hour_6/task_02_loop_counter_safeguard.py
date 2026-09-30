"""
PRACTICAL CHALLENGE: Maximum Iteration Loop Safeguard (LC-H6-P02)
=====================================================
ID: LC-H6-P02
Curriculum Tier: Advanced | Focus: LangGraph Loops & Document Crafter Agent
Task:
Implement a guard function `check_iteration_limit(state, max_iterations=5)` that increments
`state['loop_count']` and returns True if loop should continue, or raises/returns False if limit is exceeded.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def check_iteration_limit(state: dict, max_iterations: int = 5) -> bool:
    count = state.get("loop_count", 0) + 1
    state["loop_count"] = count
    if count > max_iterations:
        state["status"] = "MAX_ITERATIONS_REACHED"
        return False
    return True

def test_loop_counter():
    state = {"loop_count": 0}
    for _ in range(5):
        assert check_iteration_limit(state, max_iterations=5) is True
    
    # 6th iteration hits limit
    assert check_iteration_limit(state, max_iterations=5) is False
    assert state["status"] == "MAX_ITERATIONS_REACHED"

if __name__ == '__main__':
    test_loop_counter()
    print("✓ Task 02 passed!")
