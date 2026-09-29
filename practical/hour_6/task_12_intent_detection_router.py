"""
PRACTICAL CHALLENGE: Multi-Intent Classifier in LangGraph (LC-H6-P12)
=====================================================
ID: LC-H6-P12
Curriculum Tier: Advanced | Focus: LangGraph Loops & Document Crafter Agent
Task:
Implement an intent classifier `classify_document_action(user_text)` that categorizes
input into `['CREATE', 'UPDATE', 'SAVE', 'QUERY', 'UNKNOWN']`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def classify_document_action(text: str) -> str:
    low = text.lower()
    if any(k in low for k in ["save", "export", "download", "write to file"]):
        return "SAVE"
    if any(k in low for k in ["update", "modify", "change", "rewrite", "add"]):
        return "UPDATE"
    if any(k in low for k in ["create", "draft", "write me", "generate", "start"]):
        return "CREATE"
    if any(k in low for k in ["what", "show", "view", "read"]):
        return "QUERY"
    return "UNKNOWN"

def test_intent_detection():
    assert classify_document_action("Please draft a resignation letter") == "CREATE"
    assert classify_document_action("Change the notice period to 30 days") == "UPDATE"
    assert classify_document_action("Save document as resignation.txt") == "SAVE"
    assert classify_document_action("What is the current word count?") == "QUERY"
    assert classify_document_action("Random greeting") == "UNKNOWN"

if __name__ == '__main__':
    test_intent_detection()
    print("✓ Task 12 passed!")
