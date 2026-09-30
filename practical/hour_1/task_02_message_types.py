"""
PRACTICAL CHALLENGE: LangChain Base Message Types (LC-H1-P02)
=====================================================
ID: LC-H1-P02
Curriculum Tier: Beginner | Focus: LangChain Setup & Prompts
Task:
Implement core LangChain message classes: `BaseMessage`, `SystemMessage`, `HumanMessage`, and `AIMessage`.
Each message must store `content` and return its canonical `role` ('system', 'human', or 'ai').

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class BaseMessage:
    def __init__(self, content: str):
        self.content = content

    @property
    def role(self) -> str:
        raise NotImplementedError

class SystemMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "system"

class HumanMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "human"

class AIMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "ai"

def test_message_types():
    sys_msg = SystemMessage("You are an expert tutor.")
    human_msg = HumanMessage("Explain LLMs.")
    ai_msg = AIMessage("LLMs are neural networks...")

    assert sys_msg.role == "system" and sys_msg.content == "You are an expert tutor."
    assert human_msg.role == "human" and human_msg.content == "Explain LLMs."
    assert ai_msg.role == "ai" and "neural networks" in ai_msg.content

if __name__ == '__main__':
    test_message_types()
    print("✓ Task 02 passed!")
