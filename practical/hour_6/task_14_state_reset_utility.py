"""
PRACTICAL CHALLENGE: State Reset & Garbage Collection (LC-H6-P14)
=====================================================
ID: LC-H6-P14
Curriculum Tier: Advanced | Focus: LangGraph Loops & Document Crafter Agent
Task:
Implement `reset_document_session(state, preserve_history=False)` that resets draft content
and iteration count while optionally archiving prior messages.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def reset_document_session(state: dict, preserve_history: bool = False) -> dict:
    new_state = {
        "document_content": "",
        "revision_count": 0,
        "status": "INITIALIZED"
    }
    if preserve_history:
        new_state["archived_messages"] = list(state.get("messages", []))
        new_state["messages"] = []
    else:
        new_state["messages"] = []
    return new_state

def test_state_reset():
    active_state = {
        "document_content": "Old Draft",
        "revision_count": 4,
        "messages": [{"role": "user", "content": "draft 1"}]
    }

    fresh = reset_document_session(active_state, preserve_history=True)
    assert fresh["document_content"] == ""
    assert fresh["revision_count"] == 0
    assert len(fresh["archived_messages"]) == 1

if __name__ == '__main__':
    test_state_reset()
    print("✓ Task 14 passed!")
