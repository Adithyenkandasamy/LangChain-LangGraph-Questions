"""
PRACTICAL CHALLENGE: Complete Document Ingestion Pipeline (LC-H3-P15)
=====================================================
ID: LC-H3-P15
Curriculum Tier: Intermediate | Focus: Document Ingestion & Vector Storage
Task:
Build an end-to-end ingestion pipeline:
1. Load raw simulated text
2. Split into overlapping chunks with metadata
3. Index chunks into vector store
4. Perform similarity search and return relevant document chunks.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
from task_01_document_model import Document
from task_08_split_documents import SimpleSplitter, split_documents
from task_12_in_memory_vector_store import InMemoryVectorStore

def run_ingestion_pipeline(raw_text: str, source_id: str, query: str) -> list:
    # 1. Wrap in document
    doc = Document(raw_text, {"source": source_id})
    # 2. Split
    splitter = SimpleSplitter(chunk_size=30)
    chunks = split_documents([doc], splitter)
    # 3. Index
    store = InMemoryVectorStore()
    store.add_documents(chunks)
    # 4. Search
    return store.similarity_search(query, k=2)

def test_ingestion_pipeline():
    raw = "LangChain is designed for building context-aware reasoning applications using LLMs."
    relevant = run_ingestion_pipeline(raw, "overview.md", "context-aware applications")

    assert len(relevant) > 0
    assert relevant[0].metadata["source"] == "overview.md"

if __name__ == '__main__':
    test_ingestion_pipeline()
    print("✓ Task 15 passed!")
