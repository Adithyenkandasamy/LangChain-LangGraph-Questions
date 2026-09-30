"""
PRACTICAL CHALLENGE: ToolMessage Output Wrapper (LC-H5-P03)
=====================================================
ID: LC-H5-P03
Curriculum Tier: Advanced | Focus: Tool Calling & LangGraph Basics
Task:
Implement `ToolMessage` storing `content` (str), `tool_call_id` (str), and `role='tool'`.
Validate that `tool_call_id` matches the originating call id.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class ToolMessage:
    def __init__(self, content: str, tool_call_id: str):
        if not tool_call_id or not isinstance(tool_call_id, str):
            raise ValueError("tool_call_id must be provided.")
        self.content = str(content)
        self.tool_call_id = tool_call_id

    @property
    def role(self) -> str:
        return "tool"

def test_tool_message():
    t_msg = ToolMessage(content="Result: 42", tool_call_id="call_abc")
    assert t_msg.role == "tool"
    assert t_msg.content == "Result: 42"
    assert t_msg.tool_call_id == "call_abc"

    try:
        ToolMessage(content="fail", tool_call_id="")
        assert False, "Should raise ValueError for empty tool_call_id"
    except ValueError:
        pass

if __name__ == '__main__':
    test_tool_message()
    print("✓ Task 03 passed!")
