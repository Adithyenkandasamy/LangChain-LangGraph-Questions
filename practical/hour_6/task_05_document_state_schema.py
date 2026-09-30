"""
PRACTICAL CHALLENGE: Document Crafter State Schema (LC-H6-P05)
=====================================================
ID: LC-H6-P05
Curriculum Tier: Advanced | Focus: LangGraph Loops & Document Crafter Agent
Task:
Define a Document Crafter State schema containing:
- `messages`: list of conversation messages
- `document_content`: current draft string
- `revision_count`: integer tracking revisions.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
from typing import TypedDict, List

class DocumentCrafterState(TypedDict):
    messages: List[dict]
    document_content: str
    revision_count: int

def init_document_state(prompt: str) -> DocumentCrafterState:
    return {
        "messages": [{"role": "user", "content": prompt}],
        "document_content": "",
        "revision_count": 0
    }

def test_document_state():
    state = init_document_state("Draft a leave application")
    assert state["document_content"] == ""
    assert state["revision_count"] == 0
    assert len(state["messages"]) == 1

if __name__ == '__main__':
    test_document_state()
    print("✓ Task 05 passed!")
