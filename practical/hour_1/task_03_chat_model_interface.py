"""
PRACTICAL CHALLENGE: Chat Model Abstraction & Invocation (LC-H1-P03)
=====================================================
ID: LC-H1-P03
Curriculum Tier: Beginner | Focus: LangChain Setup & Prompts
Task:
Implement a `MockChatGoogleGenerativeAI` model that accepts a model name (e.g. 'gemini-1.5-flash')
and temperature. Its `.invoke(messages)` method should accept a list of messages and return an `AIMessage`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class BaseMessage:
    def __init__(self, content: str):
        self.content = content

class AIMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "ai"

class MockChatGoogleGenerativeAI:
    def __init__(self, model: str = "gemini-1.5-flash", temperature: float = 0.7):
        self.model = model
        self.temperature = temperature

    def invoke(self, messages):
        if not messages:
            raise ValueError("Messages list cannot be empty.")
        last_message = messages[-1]
        response_content = f"Response from {self.model} to: {last_message.content}"
        return AIMessage(response_content)

def test_model_invoke():
    model = MockChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)
    assert model.model == "gemini-1.5-flash"
    assert model.temperature == 0.2

    msg = BaseMessage("What is LangChain?")
    response = model.invoke([msg])
    assert isinstance(response, AIMessage)
    assert "Response from gemini-1.5-flash to: What is LangChain?" == response.content

if __name__ == '__main__':
    test_model_invoke()
    print("✓ Task 03 passed!")
