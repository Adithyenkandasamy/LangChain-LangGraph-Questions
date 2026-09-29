"""
PRACTICAL CHALLENGE: Compiling StateGraph to Executable App (LC-H5-P12)
=====================================================
ID: LC-H5-P12
Curriculum Tier: Advanced | Focus: Tool Calling & LangGraph Basics
Task:
Implement `.compile()` on `StateGraph` returning a `CompiledGraph` instance
with an `.invoke(initial_state)` method that runs linear node steps.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class CompiledGraph:
    def __init__(self, nodes: dict, execution_order: list):
        self.nodes = nodes
        self.execution_order = execution_order

    def invoke(self, state: dict) -> dict:
        current_state = dict(state)
        for node_name in self.execution_order:
            node_fn = self.nodes[node_name]
            updates = node_fn(current_state)
            current_state.update(updates)
        return current_state

def test_compile_graph():
    nodes = {
        "step_a": lambda s: {"val": s["val"] + 10},
        "step_b": lambda s: {"val": s["val"] * 2}
    }
    app = CompiledGraph(nodes, ["step_a", "step_b"])
    result = app.invoke({"val": 5})

    # (5 + 10) * 2 = 30
    assert result["val"] == 30

if __name__ == '__main__':
    test_compile_graph()
    print("✓ Task 12 passed!")
