"""
PRACTICAL CHALLENGE: Message Pretty-Printer Utility (LC-H6-P09)
=====================================================
ID: LC-H6-P09
Curriculum Tier: Advanced | Focus: LangGraph Loops & Document Crafter Agent
Task:
Implement `print_messages(messages)` from the lecture that formats human, AI, and tool
messages with clear visual delimiters and color tags.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def format_message_display(msg: dict) -> str:
    role = msg.get("role", "unknown").upper()
    content = msg.get("content", "")
    if "tool_calls" in msg and msg["tool_calls"]:
        calls = ", ".join([c.get("name", "") for c in msg["tool_calls"]])
        return f"[{role}] -> ToolCall: {calls}"
    return f"[{role}]: {content}"

def print_messages(messages: list) -> str:
    if not messages:
        return "No messages."
    lines = [format_message_display(m) for m in messages]
    return "\n---\n".join(lines)

def test_print_messages():
    msgs = [
        {"role": "user", "content": "Need an email draft"},
        {"role": "ai", "content": "Here is the draft"},
        {"role": "ai", "tool_calls": [{"name": "save_file"}]}
    ]
    formatted = print_messages(msgs)
    assert "[USER]: Need an email draft" in formatted
    assert "[AI]: Here is the draft" in formatted
    assert "[AI] -> ToolCall: save_file" in formatted

if __name__ == '__main__':
    test_print_messages()
    print("✓ Task 09 passed!")
