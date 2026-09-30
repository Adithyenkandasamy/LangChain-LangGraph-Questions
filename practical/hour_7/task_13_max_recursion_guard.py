"""
PRACTICAL CHALLENGE: Agent Graph Max Recursion Guard (LC-H7-P13)
=====================================================
ID: LC-H7-P13
Curriculum Tier: Mastery | Focus: Autonomous LangGraph RAG Agent
Task:
Implement `GraphRecursionGuard(max_depth=10)` class that tracks graph node transitions
and raises a `RecursionError` if transitions exceed `max_depth`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class GraphRecursionGuard:
    def __init__(self, max_depth: int = 10):
        self.max_depth = max_depth
        self.current_depth = 0

    def step(self, node_name: str):
        self.current_depth += 1
        if self.current_depth > self.max_depth:
            raise RecursionError(f"Maximum graph recursion depth ({self.max_depth}) exceeded at node '{node_name}'.")

    def reset(self):
        self.current_depth = 0

def test_recursion_guard():
    guard = GraphRecursionGuard(max_depth=3)
    guard.step("node_1")
    guard.step("node_2")
    guard.step("node_1")
    try:
        guard.step("node_2")
        assert False, "Should have raised RecursionError"
    except RecursionError as e:
        assert "depth (3) exceeded" in str(e)

if __name__ == '__main__':
    test_recursion_guard()
    print("✓ Task 13 passed!")
