"""
PRACTICAL CHALLENGE: Recursive Text Splitter with Chunk Metadata (LC-H7-P02)
=====================================================
ID: LC-H7-P02
Curriculum Tier: Mastery | Focus: Autonomous LangGraph RAG Agent
Task:
Implement `split_documents_with_metadata(documents, chunk_size=50, chunk_overlap=10)`
that splits long documents into smaller chunks while preserving and updating chunk metadata (`chunk_id`).

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class SimpleDoc:
    def __init__(self, page_content: str, metadata: dict = None):
        self.page_content = page_content
        self.metadata = dict(metadata or {})

def split_documents_with_metadata(documents: list, chunk_size: int = 50, chunk_overlap: int = 10) -> list:
    chunks = []
    chunk_counter = 0
    step = chunk_size - chunk_overlap
    if step <= 0:
        step = chunk_size
    
    for doc in documents:
        text = doc.page_content
        if len(text) <= chunk_size:
            meta = dict(doc.metadata)
            meta["chunk_id"] = chunk_counter
            chunk_counter += 1
            chunks.append(SimpleDoc(text, meta))
        else:
            for start in range(0, len(text), step):
                part = text[start:start + chunk_size]
                if not part:
                    continue
                meta = dict(doc.metadata)
                meta["chunk_id"] = chunk_counter
                chunk_counter += 1
                chunks.append(SimpleDoc(part, meta))
    return chunks

def test_chunking():
    doc = SimpleDoc("LangGraph is a library for building stateful multi-actor applications with LLMs.", {"source": "manual.pdf"})
    chunks = split_documents_with_metadata([doc], chunk_size=30, chunk_overlap=5)
    assert len(chunks) > 1
    for i, c in enumerate(chunks):
        assert c.metadata["chunk_id"] == i
        assert c.metadata["source"] == "manual.pdf"

if __name__ == '__main__':
    test_chunking()
    print("✓ Task 02 passed!")
