"""
PRACTICAL CHALLENGE: Tool Dispatcher & ToolMessage Generator (LC-H5-P05)
=====================================================
ID: LC-H5-P05
Curriculum Tier: Advanced | Focus: Tool Calling & LangGraph Basics
Task:
Implement `dispatch_tool_calls(tool_calls, tools_map)` that executes each tool call
and returns a list of corresponding `ToolMessage` instances.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
from task_03_tool_message import ToolMessage

def dispatch_tool_calls(tool_calls: list, tools_map: dict) -> list:
    tool_messages = []
    for tc in tool_calls:
        name = tc["name"]
        call_id = tc["id"]
        args = tc.get("args", {})
        if name not in tools_map:
            out = f"Error: Tool '{name}' not found."
        else:
            try:
                fn = tools_map[name]
                out = str(fn(**args))
            except Exception as e:
                out = f"Execution error: {str(e)}"
        tool_messages.append(ToolMessage(content=out, tool_call_id=call_id))
    return tool_messages

def test_tool_dispatcher():
    tools = {
        "add": lambda a, b: a + b,
        "greet": lambda name: f"Hello, {name}!"
    }
    calls = [
        {"name": "add", "args": {"a": 10, "b": 15}, "id": "c1"},
        {"name": "greet", "args": {"name": "Bob"}, "id": "c2"}
    ]
    results = dispatch_tool_calls(calls, tools)

    assert len(results) == 2
    assert results[0].content == "25" and results[0].tool_call_id == "c1"
    assert results[1].content == "Hello, Bob!" and results[1].tool_call_id == "c2"

if __name__ == '__main__':
    test_tool_dispatcher()
    print("✓ Task 05 passed!")
