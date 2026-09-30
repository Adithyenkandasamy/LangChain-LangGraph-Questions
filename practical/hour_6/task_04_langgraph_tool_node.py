"""
PRACTICAL CHALLENGE: LangGraph ToolNode Execution Pattern (LC-H6-P04)
=====================================================
ID: LC-H6-P04
Curriculum Tier: Advanced | Focus: LangGraph Loops & Document Crafter Agent
Task:
Implement a `ToolNode` class that executes tool calls from the state's latest message
and returns updated state with appended tool messages.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class ToolNode:
    def __init__(self, tools_dict: dict):
        self.tools = tools_dict

    def invoke(self, state: dict) -> dict:
        messages = list(state.get("messages", []))
        last_msg = messages[-1]
        tool_calls = last_msg.get("tool_calls", [])

        new_tool_messages = []
        for call in tool_calls:
            fn = self.tools.get(call["name"])
            if fn:
                res = fn(**call["args"])
            else:
                res = f"Tool {call['name']} not found"
            new_tool_messages.append({"role": "tool", "content": str(res), "id": call["id"]})

        messages.extend(new_tool_messages)
        return {"messages": messages}

def test_tool_node():
    node = ToolNode({"calc": lambda x: x * 10})
    state = {
        "messages": [
            {"role": "ai", "tool_calls": [{"name": "calc", "args": {"x": 5}, "id": "call_10"}]}
        ]
    }
    updated = node.invoke(state)
    assert len(updated["messages"]) == 2
    assert updated["messages"][1]["role"] == "tool"
    assert updated["messages"][1]["content"] == "50"

if __name__ == '__main__':
    test_tool_node()
    print("✓ Task 04 passed!")
