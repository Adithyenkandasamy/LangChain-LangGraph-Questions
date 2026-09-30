"""
PRACTICAL CHALLENGE: Complete Document Crafter Agent Loop (LC-H6-P15)
=====================================================
ID: LC-H6-P15
Curriculum Tier: Advanced | Focus: LangGraph Loops & Document Crafter Agent
Task:
Assemble the complete Document Crafter loop:
1. Receives initial prompt -> Creates draft
2. Receives update commands -> Applies revisions
3. Receives save command -> Persists document and outputs final state.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
from task_06_document_create_node import create_document_node
from task_07_document_update_node import update_document_node
from task_08_document_save_node import save_document_node
from task_12_intent_detection_router import classify_document_action

class DocumentCrafterAgent:
    def __init__(self):
        self.state = {"messages": [], "document_content": "", "revision_count": 0}

    def process_input(self, user_text: str, filename: str = "output.txt") -> dict:
        self.state["messages"].append({"role": "user", "content": user_text})
        action = classify_document_action(user_text)

        if action == "CREATE":
            updates = create_document_node(self.state)
            self.state.update(updates)
        elif action == "UPDATE":
            updates = update_document_node(self.state, user_text)
            self.state.update(updates)
        elif action == "SAVE":
            updates = save_document_node(self.state, filename)
            self.state.update(updates)
        return self.state

def test_document_agent():
    agent = DocumentCrafterAgent()
    s1 = agent.process_input("Create a project proposal draft")
    assert s1["revision_count"] == 1
    assert "Regarding: Create a project proposal draft" in s1["document_content"]

    s2 = agent.process_input("Update timeline to 6 months")
    assert s2["revision_count"] == 2
    assert "timeline to 6 months" in s2["document_content"]

    s3 = agent.process_input("Save proposal to file", filename="proposal.txt")
    assert s3["status"] == "SAVED"
    assert s3["saved_filename"] == "proposal.txt"

if __name__ == '__main__':
    test_document_agent()
    print("✓ Task 15 passed!")
