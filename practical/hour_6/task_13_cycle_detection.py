"""
PRACTICAL CHALLENGE: Detecting Repetitive Tool Calling Loops (LC-H6-P13)
=====================================================
ID: LC-H6-P13
Curriculum Tier: Advanced | Focus: LangGraph Loops & Document Crafter Agent
Task:
Implement `detect_tool_cycle(tool_history, max_consecutive=3)` that flags when the exact same
tool and argument signature is called repeatedly without progress.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def detect_tool_cycle(history: list, max_consecutive: int = 3) -> bool:
    if len(history) < max_consecutive:
        return False
    recent = history[-max_consecutive:]
    first = recent[0]
    return all(item == first for item in recent)

def test_cycle_detection():
    call1 = {"name": "search", "query": "python"}
    call2 = {"name": "search", "query": "langgraph"}

    assert detect_tool_cycle([call1, call1], max_consecutive=3) is False
    assert detect_tool_cycle([call1, call1, call1], max_consecutive=3) is True
    assert detect_tool_cycle([call1, call2, call1], max_consecutive=3) is False

if __name__ == '__main__':
    test_cycle_detection()
    print("✓ Task 13 passed!")
