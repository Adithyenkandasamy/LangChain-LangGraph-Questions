"""
PRACTICAL CHALLENGE: Registering Linear Edges (LC-H5-P10)
=====================================================
ID: LC-H5-P10
Curriculum Tier: Advanced | Focus: Tool Calling & LangGraph Basics
Task:
Implement `.add_edge(start_node, end_node)` on `StateGraph` and support special markers
`START` and `END`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
START = "__start__"
END = "__end__"

class StateGraphWithEdges:
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def add_node(self, name: str):
        self.nodes.add(name)

    def add_edge(self, start: str, end: str):
        if start != START and start not in self.nodes:
            raise KeyError(f"Start node '{start}' not defined.")
        if end != END and end not in self.nodes:
            raise KeyError(f"End node '{end}' not defined.")
        self.edges.append((start, end))

def test_linear_edges():
    g = StateGraphWithEdges()
    g.add_node("llm")
    g.add_node("formatter")

    g.add_edge(START, "llm")
    g.add_edge("llm", "formatter")
    g.add_edge("formatter", END)

    assert (START, "llm") in g.edges
    assert ("formatter", END) in g.edges

if __name__ == '__main__':
    test_linear_edges()
    print("✓ Task 10 passed!")
