"""
PRACTICAL CHALLENGE: PDF Document Loader & Page Ingestion (LC-H7-P01)
=====================================================
ID: LC-H7-P01
Curriculum Tier: Mastery | Focus: Autonomous LangGraph RAG Agent
Task:
Implement a loader `PDFIngestionLoader(filepath)` that reads or parses document content,
returning a list of document objects containing `page_content` and `metadata` (e.g., page number and source).

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class Document:
    def __init__(self, page_content: str, metadata: dict = None):
        self.page_content = page_content
        self.metadata = metadata or {}

class PDFIngestionLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load(self, mock_pages=None) -> list:
        if mock_pages is None:
            mock_pages = [
                "LangGraph enables building robust stateful multi-agent workflows.",
                "Retrieval-Augmented Generation (RAG) augments LLMs with factual external knowledge.",
                "Tool calling enables agents to query vector databases dynamically."
            ]
        docs = []
        for idx, text in enumerate(mock_pages):
            docs.append(Document(page_content=text, metadata={"source": self.filepath, "page": idx + 1}))
        return docs

def test_pdf_loader():
    loader = PDFIngestionLoader("course_notes.pdf")
    docs = loader.load()
    assert len(docs) == 3
    assert docs[0].metadata["source"] == "course_notes.pdf"
    assert docs[0].metadata["page"] == 1
    assert "LangGraph" in docs[0].page_content

if __name__ == '__main__':
    test_pdf_loader()
    print("✓ Task 01 passed!")
