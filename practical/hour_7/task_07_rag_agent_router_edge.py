"""
PRACTICAL CHALLENGE: RAG Agent Conditional Router Edge (LC-H7-P07)
=====================================================
ID: LC-H7-P07
Curriculum Tier: Mastery | Focus: Autonomous LangGraph RAG Agent
Task:
Implement `should_continue(state)` routing function:
If the last message contains `tool_calls`, return `'tools'`;
Otherwise, return `'end'`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def should_continue(state: dict) -> str:
    messages = state.get("messages", [])
    if not messages:
        return "end"
    last_msg = messages[-1]
    tool_calls = last_msg.get("tool_calls")
    if tool_calls and len(tool_calls) > 0:
        return "tools"
    return "end"

def test_router():
    s1 = {"messages": [{"role": "assistant", "tool_calls": [{"name": "search"}]}]}
    assert should_continue(s1) == "tools"

    s2 = {"messages": [{"role": "assistant", "content": "All clear."}]}
    assert should_continue(s2) == "end"

if __name__ == '__main__':
    test_router()
    print("✓ Task 07 passed!")
