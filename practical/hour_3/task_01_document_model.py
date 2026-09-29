"""
PRACTICAL CHALLENGE: Core Document Representation (LC-H3-P01)
=====================================================
ID: LC-H3-P01
Curriculum Tier: Intermediate | Focus: Document Ingestion & Vector Storage
Task:
Implement a `Document` class storing `page_content` (str) and `metadata` (dict).
Ensure default metadata is an empty dictionary and equality checks compare both content and metadata.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class Document:
    def __init__(self, page_content: str, metadata: dict = None):
        self.page_content = page_content
        self.metadata = metadata if metadata is not None else {}

    def __eq__(self, other):
        if not isinstance(other, Document):
            return False
        return self.page_content == other.page_content and self.metadata == other.metadata

def test_document():
    doc1 = Document("LangChain is a framework.", {"source": "intro.txt", "page": 1})
    doc2 = Document("LangChain is a framework.", {"source": "intro.txt", "page": 1})
    doc3 = Document("Different content.", {"source": "intro.txt", "page": 1})

    assert doc1.page_content == "LangChain is a framework."
    assert doc1.metadata["source"] == "intro.txt"
    assert doc1 == doc2
    assert doc1 != doc3

if __name__ == '__main__':
    test_document()
    print("✓ Task 01 passed!")
