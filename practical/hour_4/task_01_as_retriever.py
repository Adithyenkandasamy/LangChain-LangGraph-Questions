"""
PRACTICAL CHALLENGE: Vector Store as_retriever Converter (LC-H4-P01)
=====================================================
ID: LC-H4-P01
Curriculum Tier: Advanced | Focus: Advanced RAG & Tool Interfaces
Task:
Implement `.as_retriever(search_type='similarity', search_kwargs={'k': 2})` on a VectorStore
that wraps search queries into a `Retriever` object supporting `.invoke(query)`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class MockVectorStore:
    def __init__(self, sample_docs: list):
        self.sample_docs = sample_docs

    def similarity_search(self, query: str, k: int = 2) -> list:
        # return top k matching query substring or default
        matches = [d for d in self.sample_docs if any(w.lower() in d.lower() for w in query.split())]
        return (matches or self.sample_docs)[:k]

    def as_retriever(self, search_kwargs: dict = None):
        return VectorStoreRetriever(self, search_kwargs or {"k": 2})

class VectorStoreRetriever:
    def __init__(self, vector_store: MockVectorStore, search_kwargs: dict):
        self.vector_store = vector_store
        self.search_kwargs = search_kwargs

    def invoke(self, query: str) -> list:
        k = self.search_kwargs.get("k", 2)
        return self.vector_store.similarity_search(query, k=k)

def test_as_retriever():
    store = MockVectorStore(["LangChain Core", "LangChain Community", "LangGraph"])
    retriever = store.as_retriever(search_kwargs={"k": 2})

    results = retriever.invoke("Core")
    assert len(results) <= 2
    assert "LangChain Core" in results

if __name__ == '__main__':
    test_as_retriever()
    print("✓ Task 01 passed!")
