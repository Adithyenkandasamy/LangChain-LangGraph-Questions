"""
PRACTICAL CHALLENGE: Document Creation Node (LC-H6-P06)
=====================================================
ID: LC-H6-P06
Curriculum Tier: Advanced | Focus: LangGraph Loops & Document Crafter Agent
Task:
Implement a `create_document_node(state)` that generates initial document content
from the user's prompt and sets `revision_count` to 1.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def create_document_node(state: dict) -> dict:
    user_prompt = state["messages"][-1]["content"]
    draft = f"Subject: Official Notice\n\nDear Team,\n\nRegarding: {user_prompt}\n\nSincerely,\nManagement"
    return {
        "document_content": draft,
        "revision_count": 1,
        "messages": state["messages"] + [{"role": "ai", "content": "Draft created successfully."}]
    }

def test_create_document_node():
    initial = {"messages": [{"role": "user", "content": "Holiday Schedule"}], "revision_count": 0}
    result = create_document_node(initial)

    assert result["revision_count"] == 1
    assert "Regarding: Holiday Schedule" in result["document_content"]
    assert len(result["messages"]) == 2

if __name__ == '__main__':
    test_create_document_node()
    print("✓ Task 06 passed!")
