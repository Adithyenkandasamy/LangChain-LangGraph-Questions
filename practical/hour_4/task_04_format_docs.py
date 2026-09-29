"""
PRACTICAL CHALLENGE: Formatting Documents for Context Injection (LC-H4-P04)
=====================================================
ID: LC-H4-P04
Curriculum Tier: Advanced | Focus: Advanced RAG & Tool Interfaces
Task:
Implement `format_docs(docs)` that concatenates a list of document objects into a clean,
numbered or separated context string with source references.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class MockDoc:
    def __init__(self, content: str, source: str):
        self.page_content = content
        self.metadata = {"source": source}

def format_docs(docs: list) -> str:
    parts = []
    for idx, doc in enumerate(docs, start=1):
        source = doc.metadata.get("source", "Unknown")
        parts.append(f"[{idx}] (Source: {source})\n{doc.page_content.strip()}")
    return "\n\n".join(parts)

def test_format_docs():
    docs = [
        MockDoc("LangChain simplifies prompt management.", "chap1.pdf"),
        MockDoc("Vector stores index embeddings efficiently.", "chap2.pdf")
    ]
    formatted = format_docs(docs)
    assert "[1] (Source: chap1.pdf)" in formatted
    assert "[2] (Source: chap2.pdf)" in formatted
    assert "Vector stores index embeddings efficiently." in formatted

if __name__ == '__main__':
    test_format_docs()
    print("✓ Task 04 passed!")
