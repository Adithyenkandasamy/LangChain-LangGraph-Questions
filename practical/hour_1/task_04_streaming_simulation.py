"""
PRACTICAL CHALLENGE: Simulating Model Streaming Chunks (LC-H1-P04)
=====================================================
ID: LC-H1-P04
Curriculum Tier: Beginner | Focus: LangChain Setup & Prompts
Task:
Implement a streaming method `.stream(prompt)` on the chat model that yields token chunks
as small string tokens, allowing consumers to process tokens incrementally.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class MockStreamingChatModel:
    def __init__(self, model_name: str = "gemini-1.5-flash"):
        self.model_name = model_name

    def stream(self, prompt: str):
        words = f"Echo: {prompt}".split()
        for word in words:
            yield word + " "

def test_streaming():
    model = MockStreamingChatModel()
    chunks = list(model.stream("Hello world from LangChain"))
    assert len(chunks) == 5
    accumulated = "".join(chunks).strip()
    assert accumulated == "Echo: Hello world from LangChain"

if __name__ == '__main__':
    test_streaming()
    print("✓ Task 04 passed!")
