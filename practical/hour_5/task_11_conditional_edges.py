"""
PRACTICAL CHALLENGE: Conditional Edges Routing (LC-H5-P11)
=====================================================
ID: LC-H5-P11
Curriculum Tier: Advanced | Focus: Tool Calling & LangGraph Basics
Task:
Implement `.add_conditional_edges(source, condition_fn, path_map)` that evaluates state
and maps condition return value to the next target node.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class ConditionalGraphRouter:
    def __init__(self):
        self.conditional_edges = {}

    def add_conditional_edges(self, source: str, condition_fn, path_map: dict):
        self.conditional_edges[source] = (condition_fn, path_map)

    def route_next(self, source: str, state: dict) -> str:
        condition_fn, path_map = self.conditional_edges[source]
        decision = condition_fn(state)
        return path_map[decision]

def test_conditional_edges():
    router = ConditionalGraphRouter()
    
    def check_tools(state):
        return "has_tools" if state.get("tool_calls") else "finish"

    router.add_conditional_edges(
        "agent",
        check_tools,
        {"has_tools": "tools_node", "finish": "end_node"}
    )

    next_with_tools = router.route_next("agent", {"tool_calls": ["call1"]})
    assert next_with_tools == "tools_node"

    next_no_tools = router.route_next("agent", {"tool_calls": []})
    assert next_no_tools == "end_node"

if __name__ == '__main__':
    test_conditional_edges()
    print("✓ Task 11 passed!")
