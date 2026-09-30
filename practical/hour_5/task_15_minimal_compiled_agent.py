"""
PRACTICAL CHALLENGE: Minimal End-to-End StateGraph Agent (LC-H5-P15)
=====================================================
ID: LC-H5-P15
Curriculum Tier: Advanced | Focus: Tool Calling & LangGraph Basics
Task:
Assemble a minimal compiled StateGraph with:
- Start -> 'agent_node' -> 'router'
- Router routes to 'tool_node' if tool call present, else END
- 'tool_node' routes back to 'agent_node'.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class SimpleStateGraphAgent:
    def __init__(self, tool_func):
        self.tool_func = tool_func

    def run(self, prompt: str) -> dict:
        state = {"messages": [prompt], "iterations": 0}

        while state["iterations"] < 5:
            state["iterations"] += 1
            last = state["messages"][-1]

            if "calculate" in last:
                # agent decides to call tool
                res = self.tool_func(last)
                state["messages"].append(f"Tool Result: {res}")
            else:
                # agent finishes
                state["messages"].append("Final Answer: Completed.")
                break

        return state

def test_minimal_graph_agent():
    agent = SimpleStateGraphAgent(lambda text: "Calculated 42")
    final_state = agent.run("Please calculate the metric")

    assert len(final_state["messages"]) == 3
    assert "Tool Result: Calculated 42" in final_state["messages"][1]
    assert "Final Answer: Completed." in final_state["messages"][2]

if __name__ == '__main__':
    test_minimal_graph_agent()
    print("✓ Task 15 passed!")
