"""
PRACTICAL CHALLENGE: Dynamic Router Node Implementation (LC-H6-P01)
=====================================================
ID: LC-H6-P01
Curriculum Tier: Advanced | Focus: LangGraph Loops & Document Crafter Agent
Task:
Implement a router node function `decide_next_node(state)` that inspects the last message
in `state["messages"]`. If the message indicates a tool call, route to 'tool_node'; if it says 'done' or 'save', route to 'end'; otherwise route to 'agent'.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def decide_next_node(state: dict) -> str:
    messages = state.get("messages", [])
    if not messages:
        return "agent"
    last_msg = messages[-1]
    if isinstance(last_msg, dict):
        if last_msg.get("tool_calls"):
            return "tool_node"
        content = last_msg.get("content", "").lower()
    else:
        content = getattr(last_msg, "content", "").lower()

    if "save" in content or "done" in content or "exit" in content:
        return "end"
    return "agent"

def test_router_node():
    assert decide_next_node({"messages": []}) == "agent"
    assert decide_next_node({"messages": [{"tool_calls": ["c1"]}]}) == "tool_node"
    assert decide_next_node({"messages": [{"content": "All done, please save."}]}) == "end"
    assert decide_next_node({"messages": [{"content": "Please rewrite the intro."}]}) == "agent"

if __name__ == '__main__':
    test_router_node()
    print("✓ Task 01 passed!")
