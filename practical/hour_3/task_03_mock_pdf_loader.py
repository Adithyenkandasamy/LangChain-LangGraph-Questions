"""
PRACTICAL CHALLENGE: PDF Document Loader Simulation (LC-H3-P03)
=====================================================
ID: LC-H3-P03
Curriculum Tier: Intermediate | Focus: Document Ingestion & Vector Storage
Task:
Implement a `MockPyPDFLoader` that parses simulated multi-page PDF records and returns
one Document per page with metadata `{'source': path, 'page': page_number}`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class Document:
    def __init__(self, page_content: str, metadata: dict = None):
        self.page_content = page_content
        self.metadata = metadata or {}

class MockPyPDFLoader:
    def __init__(self, file_path: str, simulated_pages: list = None):
        self.file_path = file_path
        self.simulated_pages = simulated_pages or []

    def load(self) -> list:
        documents = []
        for idx, page_text in enumerate(self.simulated_pages, start=1):
            documents.append(Document(
                page_content=page_text,
                metadata={"source": self.file_path, "page": idx}
            ))
        return documents

def test_pdf_loader():
    pages = ["Page 1: Architecture of RAG", "Page 2: Vector Stores & FAISS", "Page 3: Evaluation Metrics"]
    loader = MockPyPDFLoader("docs/whitepaper.pdf", simulated_pages=pages)
    docs = loader.load()

    assert len(docs) == 3
    assert docs[0].metadata["page"] == 1
    assert docs[1].page_content == "Page 2: Vector Stores & FAISS"
    assert docs[2].metadata["source"] == "docs/whitepaper.pdf"

if __name__ == '__main__':
    test_pdf_loader()
    print("✓ Task 03 passed!")
