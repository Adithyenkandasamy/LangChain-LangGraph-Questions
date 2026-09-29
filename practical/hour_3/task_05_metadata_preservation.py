"""
PRACTICAL CHALLENGE: Preserving Metadata During Transformations (LC-H3-P05)
=====================================================
ID: LC-H3-P05
Curriculum Tier: Intermediate | Focus: Document Ingestion & Vector Storage
Task:
Implement `copy_with_new_content(doc, new_content)` that creates a new `Document` with updated text
while deeply copying existing metadata and updating character count in metadata.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
import copy

class Document:
    def __init__(self, page_content: str, metadata: dict = None):
        self.page_content = page_content
        self.metadata = metadata or {}

def copy_with_new_content(doc: Document, new_content: str) -> Document:
    new_meta = copy.deepcopy(doc.metadata)
    new_meta["char_count"] = len(new_content)
    return Document(page_content=new_content, metadata=new_meta)

def test_metadata_preservation():
    original = Document("Original text", {"source": "data.csv", "author": "Alice"})
    transformed = copy_with_new_content(original, "Transformed and cleaned text")

    assert transformed.page_content == "Transformed and cleaned text"
    assert transformed.metadata["source"] == "data.csv"
    assert transformed.metadata["author"] == "Alice"
    assert transformed.metadata["char_count"] == len("Transformed and cleaned text")
    assert "char_count" not in original.metadata

if __name__ == '__main__':
    test_metadata_preservation()
    print("✓ Task 05 passed!")
