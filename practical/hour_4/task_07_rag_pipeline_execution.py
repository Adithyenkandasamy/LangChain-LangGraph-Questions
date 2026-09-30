"""
PRACTICAL CHALLENGE: End-to-End RAG Execution Simulator (LC-H4-P07)
=====================================================
ID: LC-H4-P07
Curriculum Tier: Advanced | Focus: Advanced RAG & Tool Interfaces
Task:
Implement a complete RAG chain runner:
1. Retriever fetches relevant documents for query
2. Context is formatted
3. Grounded prompt is generated
4. LLM produces answer.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
from task_04_format_docs import MockDoc, format_docs
from task_05_grounded_rag_prompt import create_rag_prompt

class MockRAGSystem:
    def __init__(self, doc_db: list):
        self.doc_db = doc_db

    def retrieve(self, query: str) -> list:
        # substring matching
        matches = [d for d in self.doc_db if any(w.lower() in d.page_content.lower() for w in query.split())]
        return matches

    def generate(self, prompt: str) -> str:
        if "Google Gemini" in prompt:
            return "Gemini is Google's multimodal AI model."
        return "I do not know"

    def ask(self, query: str) -> str:
        docs = self.retrieve(query)
        context = format_docs(docs) if docs else "No relevant context found."
        prompt = create_rag_prompt(context, query)
        return self.generate(prompt)

def test_rag_pipeline():
    docs = [
        MockDoc("Google Gemini models provide strong reasoning and multimodal understanding.", "gemini_spec.txt")
    ]
    rag = MockRAGSystem(docs)

    ans1 = rag.ask("Tell me about Google Gemini")
    assert "Gemini is Google's multimodal AI model." in ans1

    ans2 = rag.ask("What is quantum teleportation?")
    assert ans2 == "I do not know"

if __name__ == '__main__':
    test_rag_pipeline()
    print("✓ Task 07 passed!")
