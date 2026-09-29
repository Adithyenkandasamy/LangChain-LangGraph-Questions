"""
PRACTICAL CHALLENGE: Multi-Turn Chat History Buffer (LC-H1-P09)
=====================================================
ID: LC-H1-P09
Curriculum Tier: Beginner | Focus: LangChain Setup & Prompts
Task:
Implement a `ChatMessageHistory` class that stores conversation turns, allows adding user and AI messages,
and formats them for subsequent model context.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class BaseMessage:
    def __init__(self, content: str):
        self.content = content

class HumanMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "human"

class AIMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "ai"

class ChatMessageHistory:
    def __init__(self):
        self.messages = []

    def add_user_message(self, message: str):
        self.messages.append(HumanMessage(message))

    def add_ai_message(self, message: str):
        self.messages.append(AIMessage(message))

    def clear(self):
        self.messages.clear()

    def get_transcript(self) -> str:
        lines = []
        for m in self.messages:
            prefix = "User" if m.role == "human" else "AI"
            lines.append(f"{prefix}: {m.content}")
        return "\n".join(lines)

def test_chat_history():
    history = ChatMessageHistory()
    history.add_user_message("Hello, my name is Alex.")
    history.add_ai_message("Hello Alex! How can I assist you today?")
    history.add_user_message("What is my name?")

    assert len(history.messages) == 3
    transcript = history.get_transcript()
    assert "User: Hello, my name is Alex." in transcript
    assert "AI: Hello Alex!" in transcript

if __name__ == '__main__':
    test_chat_history()
    print("✓ Task 09 passed!")
