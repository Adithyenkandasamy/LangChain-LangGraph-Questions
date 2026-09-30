"""
PRACTICAL CHALLENGE: Adding Nodes to StateGraph (LC-H5-P09)
=====================================================
ID: LC-H5-P09
Curriculum Tier: Advanced | Focus: Tool Calling & LangGraph Basics
Task:
Implement a `StateGraph` builder that registers nodes `graph.add_node(name, func)`
and prevents registering duplicate node names.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class StateGraph:
    def __init__(self, state_schema):
        self.state_schema = state_schema
        self.nodes = {}

    def add_node(self, name: str, func):
        if name in self.nodes:
            raise ValueError(f"Node '{name}' already exists in graph.")
        self.nodes[name] = func

def test_graph_nodes():
    graph = StateGraph(dict)
    graph.add_node("agent", lambda state: state)
    graph.add_node("tools", lambda state: state)

    assert "agent" in graph.nodes and "tools" in graph.nodes

    try:
        graph.add_node("agent", lambda state: state)
        assert False, "Should raise ValueError for duplicate node"
    except ValueError:
        pass

if __name__ == '__main__':
    test_graph_nodes()
    print("✓ Task 09 passed!")
