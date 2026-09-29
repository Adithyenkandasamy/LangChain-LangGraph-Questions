"""
PRACTICAL CHALLENGE: Splitting Documents with Metadata Propagation (LC-H3-P08)
=====================================================
ID: LC-H3-P08
Curriculum Tier: Intermediate | Focus: Document Ingestion & Vector Storage
Task:
Implement `split_documents(docs, splitter)` which takes a list of `Document`s,
splits each document's text using the splitter, and propagates the original metadata to all resulting chunks.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class Document:
    def __init__(self, page_content: str, metadata: dict = None):
        self.page_content = page_content
        self.metadata = metadata or {}

class SimpleSplitter:
    def __init__(self, chunk_size: int = 30):
        self.chunk_size = chunk_size

    def split_text(self, text: str) -> list:
        words = text.split()
        chunks = []
        curr = []
        curr_len = 0
        for w in words:
            if curr_len + len(w) + 1 <= self.chunk_size:
                curr.append(w)
                curr_len += len(w) + 1
            else:
                if curr: chunks.append(" ".join(curr))
                curr = [w]
                curr_len = len(w)
        if curr: chunks.append(" ".join(curr))
        return chunks

def split_documents(docs: list, splitter) -> list:
    out = []
    for doc in docs:
        chunks = splitter.split_text(doc.page_content)
        for idx, chunk in enumerate(chunks):
            meta = dict(doc.metadata)
            meta["chunk_index"] = idx
            out.append(Document(chunk, meta))
    return out

def test_split_documents():
    docs = [
        Document("Fast and reliable indexing for AI systems.", {"source": "guide.md"}),
        Document("Short doc.", {"source": "notes.md"})
    ]
    splitter = SimpleSplitter(chunk_size=20)
    chunked_docs = split_documents(docs, splitter)

    assert len(chunked_docs) >= 2
    assert chunked_docs[0].metadata["source"] == "guide.md"
    assert "chunk_index" in chunked_docs[0].metadata
    assert chunked_docs[-1].metadata["source"] == "notes.md"

if __name__ == '__main__':
    test_split_documents()
    print("✓ Task 08 passed!")
