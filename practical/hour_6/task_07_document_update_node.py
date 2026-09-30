"""
PRACTICAL CHALLENGE: Document Revision & Update Node (LC-H6-P07)
=====================================================
ID: LC-H6-P07
Curriculum Tier: Advanced | Focus: LangGraph Loops & Document Crafter Agent
Task:
Implement `update_document_node(state, instruction)` that modifies existing `document_content`,
increments `revision_count`, and appends a revision note.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def update_document_node(state: dict, instruction: str) -> dict:
    current = state.get("document_content", "")
    updated_content = current + f"\n\n[Revision note: {instruction}]"
    revisions = state.get("revision_count", 0) + 1
    return {
        "document_content": updated_content,
        "revision_count": revisions,
        "messages": state.get("messages", []) + [{"role": "ai", "content": f"Updated for: {instruction}"}]
    }

def test_update_document_node():
    base_state = {
        "document_content": "Base Content",
        "revision_count": 1,
        "messages": []
    }
    updated = update_document_node(base_state, "Add contact phone number")

    assert updated["revision_count"] == 2
    assert "[Revision note: Add contact phone number]" in updated["document_content"]

if __name__ == '__main__':
    test_update_document_node()
    print("✓ Task 07 passed!")
