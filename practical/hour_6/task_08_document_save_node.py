"""
PRACTICAL CHALLENGE: Document Persistence Node (LC-H6-P08)
=====================================================
ID: LC-H6-P08
Curriculum Tier: Advanced | Focus: LangGraph Loops & Document Crafter Agent
Task:
Implement `save_document_node(state, filename)` that simulates writing `document_content`
to a target file and marks state with `status='SAVED'`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def save_document_node(state: dict, filename: str) -> dict:
    content = state.get("document_content", "")
    if not content.strip():
        raise ValueError("Cannot save empty document content.")
    
    # In real app writes to disk; here sets metadata
    return {
        "saved_filename": filename,
        "status": "SAVED",
        "file_size_bytes": len(content.encode("utf-8")),
        "messages": state.get("messages", []) + [{"role": "system", "content": f"Document saved as {filename}"}]
    }

def test_save_document_node():
    state = {"document_content": "Important business memorandum text.", "messages": []}
    res = save_document_node(state, "memo.txt")

    assert res["status"] == "SAVED"
    assert res["saved_filename"] == "memo.txt"
    assert res["file_size_bytes"] > 0

    try:
        save_document_node({"document_content": "   "}, "memo.txt")
        assert False, "Should raise ValueError on empty content"
    except ValueError:
        pass

if __name__ == '__main__':
    test_save_document_node()
    print("✓ Task 08 passed!")
