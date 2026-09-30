"""
PRACTICAL CHALLENGE: Interactive Multi-Turn Dialogue Simulation (LC-H1-P15)
=====================================================
ID: LC-H1-P15
Curriculum Tier: Beginner | Focus: LangChain Setup & Prompts
Task:
Implement a conversation simulation runner `simulate_conversation(user_inputs, model)` that:
1. Maintains full conversation history
2. Stops when the user types 'exit' or inputs are exhausted
3. Returns the list of all turns and final message count.

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

class MockChatModel:
    def invoke(self, messages):
        last_msg = messages[-1].content
        return AIMessage(f"Response to: {last_msg}")

def simulate_conversation(user_inputs: list, model) -> list:
    history = []
    for user_text in user_inputs:
        if user_text.strip().lower() == "exit":
            break
        human_msg = HumanMessage(user_text)
        history.append(human_msg)
        response = model.invoke(history)
        history.append(response)
    return history

def test_conversation_runner():
    model = MockChatModel()
    inputs = ["Hello", "What is LangChain?", "exit", "Should not be processed"]
    history = simulate_conversation(inputs, model)

    assert len(history) == 4
    assert history[0].role == "human" and history[0].content == "Hello"
    assert history[1].role == "ai"
    assert history[2].role == "human" and history[2].content == "What is LangChain?"
    assert history[3].role == "ai"

if __name__ == '__main__':
    test_conversation_runner()
    print("✓ Task 15 passed!")
