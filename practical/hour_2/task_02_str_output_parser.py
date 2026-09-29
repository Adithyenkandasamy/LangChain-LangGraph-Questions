"""
PRACTICAL CHALLENGE: StrOutputParser Implementation (LC-H2-P02)
=====================================================
ID: LC-H2-P02
Curriculum Tier: Intermediate | Focus: LCEL & Chain Composition
Task:
Implement StrOutputParser as a Runnable that extracts cleaned text from an AIMessage or dictionary.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class AIMessage:
    def __init__(self, content: str):
        self.content = content

class StrOutputParser:
    def invoke(self, input_val) -> str:
        if hasattr(input_val, "content"):
            return str(input_val.content).strip()
        elif isinstance(input_val, dict) and "content" in input_val:
            return str(input_val["content"]).strip()
        return str(input_val).strip()

def test_str_output_parser():
    parser = StrOutputParser()
    msg = AIMessage("  LangChain Expression Language (LCEL)  \n")
    assert parser.invoke(msg) == "LangChain Expression Language (LCEL)"
    assert parser.invoke({"content": "Hello World"}) == "Hello World"
    assert parser.invoke("Raw text") == "Raw text"

if __name__ == '__main__':
    test_str_output_parser()
    print("✓ Task 02 passed!")
