"""
PRACTICAL CHALLENGE: Basic LCEL Prompt and Model Chain (LC-H2-P03)
=====================================================
ID: LC-H2-P03
Curriculum Tier: Intermediate | Focus: LCEL & Chain Composition
Task:
Build a basic LCEL chain combining prompt, model, and parser.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class MockPrompt:
    def __init__(self, template: str):
        self.template = template
    def invoke(self, kwargs: dict) -> str:
        return self.template.format(**kwargs)

class MockModel:
    def invoke(self, text: str):
        class Msg:
            def __init__(self, content): self.content = content
        return Msg(f"Detailed answer about: {text}")

class StrOutputParser:
    def invoke(self, msg) -> str:
        return msg.content

class SimpleChain:
    def __init__(self, prompt, model, parser):
        self.prompt = prompt
        self.model = model
        self.parser = parser

    def invoke(self, inputs: dict) -> str:
        p_out = self.prompt.invoke(inputs)
        m_out = self.model.invoke(p_out)
        return self.parser.invoke(m_out)

def test_simple_chain():
    prompt = MockPrompt("Explain {topic} in one sentence.")
    model = MockModel()
    parser = StrOutputParser()
    chain = SimpleChain(prompt, model, parser)

    out = chain.invoke({"topic": "Vector Stores"})
    assert out == "Detailed answer about: Explain Vector Stores in one sentence."

if __name__ == '__main__':
    test_simple_chain()
    print("✓ Task 03 passed!")
