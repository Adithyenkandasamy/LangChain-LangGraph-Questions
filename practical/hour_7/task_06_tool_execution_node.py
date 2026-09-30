"""
PRACTICAL CHALLENGE: LangGraph Tool Execution Node (LC-H7-P06)
=====================================================
ID: LC-H7-P06
Curriculum Tier: Mastery | Focus: Autonomous LangGraph RAG Agent
Task:
Implement `execute_tool_node(state, tools_map)` that extracts tool calls from the last
assistant message, executes the matching tool, and appends a `tool` role message to state.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def execute_tool_node(state: dict, tools_map: dict) -> dict:
    messages = state["messages"]
    last_msg = messages[-1]
    tool_calls = last_msg.get("tool_calls", [])

    new_messages = []
    for tc in tool_calls:
        tool_name = tc.get("name")
        args = tc.get("args", {})
        if tool_name in tools_map:
            tool_fn = tools_map[tool_name]
            result = tool_fn(**args)
        else:
            result = f"Error: Tool {tool_name} not found."
        new_messages.append({"role": "tool", "name": tool_name, "content": result})

    state["messages"].extend(new_messages)
    return state

def test_tool_node():
    tools = {"rag_search": lambda query: f"Retrieved docs for {query}"}
    state = {
        "messages": [
            {"role": "assistant", "tool_calls": [{"name": "rag_search", "args": {"query": "LangGraph"}}]}
        ]
    }
    updated = execute_tool_node(state, tools)
    assert len(updated["messages"]) == 2
    assert updated["messages"][-1]["role"] == "tool"
    assert "Retrieved docs" in updated["messages"][-1]["content"]

if __name__ == '__main__':
    test_tool_node()
    print("✓ Task 06 passed!")
