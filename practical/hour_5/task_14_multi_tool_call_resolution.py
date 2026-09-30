"""
PRACTICAL CHALLENGE: Simultaneous Multi-Tool Resolution (LC-H5-P14)
=====================================================
ID: LC-H5-P14
Curriculum Tier: Advanced | Focus: Tool Calling & LangGraph Basics
Task:
Implement resolution of multiple tool calls issued in a single turn, preserving matching IDs
and collecting results into a single list of ToolMessages.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
from task_03_tool_message import ToolMessage

def resolve_multiple_calls(tool_calls: list, tool_registry: dict) -> list:
    out = []
    for tc in tool_calls:
        fn = tool_registry[tc["name"]]
        val = fn(**tc["args"])
        out.append(ToolMessage(content=str(val), tool_call_id=tc["id"]))
    return out

def test_multi_tool_resolution():
    registry = {
        "get_stock_price": lambda symbol: 150.0 if symbol == "AAPL" else 200.0,
        "get_pe_ratio": lambda symbol: 28.5
    }
    calls = [
        {"name": "get_stock_price", "args": {"symbol": "AAPL"}, "id": "c1"},
        {"name": "get_pe_ratio", "args": {"symbol": "AAPL"}, "id": "c2"}
    ]
    tool_messages = resolve_multiple_calls(calls, registry)

    assert len(tool_messages) == 2
    assert tool_messages[0].content == "150.0" and tool_messages[0].tool_call_id == "c1"
    assert tool_messages[1].content == "28.5" and tool_messages[1].tool_call_id == "c2"

if __name__ == '__main__':
    test_multi_tool_resolution()
    print("✓ Task 14 passed!")
