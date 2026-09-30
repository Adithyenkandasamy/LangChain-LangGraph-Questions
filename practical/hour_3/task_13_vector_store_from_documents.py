"""
PRACTICAL CHALLENGE: from_documents Factory Method (LC-H3-P13)
=====================================================
ID: LC-H3-P13
Curriculum Tier: Intermediate | Focus: Document Ingestion & Vector Storage
Task:
Implement `from_documents(documents, embedding)` factory constructor on `InMemoryVectorStore`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
from task_12_in_memory_vector_store import InMemoryVectorStore, Document
from task_10_mock_embeddings import MockEmbeddings

def create_vector_store_from_documents(documents: list, embedding_model=None):
    store = InMemoryVectorStore(embedding_model or MockEmbeddings())
    store.add_documents(documents)
    return store

def test_from_documents():
    docs = [
        Document("LangChain chains and runnables", {"topic": "chains"}),
        Document("LangGraph state and cycles", {"topic": "graph"})
    ]
    store = create_vector_store_from_documents(docs)
    assert len(store.records) == 2
    top = store.similarity_search("LangChain chains", k=1)
    assert top[0].metadata["topic"] == "chains"

if __name__ == '__main__':
    test_from_documents()
    print("✓ Task 13 passed!")
