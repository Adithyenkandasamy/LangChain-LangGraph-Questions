"""
PRACTICAL CHALLENGE: AIMessage with tool_calls Attribute (LC-H5-P02)
=====================================================
ID: LC-H5-P02
Curriculum Tier: Advanced | Focus: Tool Calling & LangGraph Basics
Task:
Implement an `AIMessage` class that supports both optional text `content` and optional `tool_calls` list.
Provide a helper property `.has_tool_calls` returning True if `tool_calls` contains at least one item.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class AIMessage:
    def __init__(self, content: str = "", tool_calls: list = None):
        self.content = content
        self.tool_calls = tool_calls or []

    @property
    def has_tool_calls(self) -> bool:
        return len(self.tool_calls) > 0

def test_ai_message_with_tools():
    msg_plain = AIMessage(content="Hello world!")
    assert not msg_plain.has_tool_calls

    msg_with_call = AIMessage(
        content="",
        tool_calls=[{"name": "fetch_stock", "args": {"symbol": "AAPL"}, "id": "call_99"}]
    )
    assert msg_with_call.has_tool_calls
    assert msg_with_call.tool_calls[0]["name"] == "fetch_stock"

if __name__ == '__main__':
    test_ai_message_with_tools()
    print("✓ Task 02 passed!")
