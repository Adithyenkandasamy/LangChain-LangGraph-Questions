"""
PRACTICAL CHALLENGE: Text File Loader Implementation (LC-H3-P02)
=====================================================
ID: LC-H3-P02
Curriculum Tier: Intermediate | Focus: Document Ingestion & Vector Storage
Task:
Implement a `TextLoader` that reads a plain text file from disk and returns a list containing
a single `Document` object with its text and metadata `{'source': file_path}`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class Document:
    def __init__(self, page_content: str, metadata: dict = None):
        self.page_content = page_content
        self.metadata = metadata or {}

class TextLoader:
    def __init__(self, file_path: str, encoding: str = "utf-8"):
        self.file_path = file_path
        self.encoding = encoding

    def load(self) -> list:
        with open(self.file_path, "r", encoding=self.encoding) as f:
            content = f.read()
        return [Document(page_content=content, metadata={"source": self.file_path})]

def test_text_loader():
    import tempfile
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".txt") as tmp:
        tmp.write("Sample document content for RAG indexing.")
        tmp_name = tmp.name

    try:
        loader = TextLoader(tmp_name)
        docs = loader.load()
        assert len(docs) == 1
        assert docs[0].page_content == "Sample document content for RAG indexing."
        assert docs[0].metadata["source"] == tmp_name
    finally:
        import os
        os.remove(tmp_name)

if __name__ == '__main__':
    test_text_loader()
    print("✓ Task 02 passed!")
