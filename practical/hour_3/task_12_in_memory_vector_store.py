"""
PRACTICAL CHALLENGE: In-Memory Vector Store Indexing (LC-H3-P12)
=====================================================
ID: LC-H3-P12
Curriculum Tier: Intermediate | Focus: Document Ingestion & Vector Storage
Task:
Implement an `InMemoryVectorStore` with `add_documents(docs)` and `similarity_search(query, k)`
using embedding vectors and cosine similarity.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
from task_10_mock_embeddings import MockEmbeddings
from task_11_cosine_similarity import cosine_similarity

class Document:
    def __init__(self, page_content: str, metadata: dict = None):
        self.page_content = page_content
        self.metadata = metadata or {}

class InMemoryVectorStore:
    def __init__(self, embedding_model=None):
        self.embedding_model = embedding_model or MockEmbeddings()
        self.records = []

    def add_documents(self, documents: list):
        texts = [d.page_content for d in documents]
        vectors = self.embedding_model.embed_documents(texts)
        for doc, vec in zip(documents, vectors):
            self.records.append({"doc": doc, "vector": vec})

    def similarity_search(self, query: str, k: int = 2) -> list:
        q_vec = self.embedding_model.embed_query(query)
        scored = []
        for rec in self.records:
            score = cosine_similarity(q_vec, rec["vector"])
            scored.append((score, rec["doc"]))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [doc for score, doc in scored[:k]]

def test_vector_store():
    store = InMemoryVectorStore()
    docs = [
        Document("LangChain vector database retrieval methods", {"id": 1}),
        Document("Cooking pasta recipes and ingredients", {"id": 2}),
        Document("Building AI agents with LLM prompts", {"id": 3})
    ]
    store.add_documents(docs)

    results = store.similarity_search("vector database", k=1)
    assert len(results) == 1
    assert "retrieval methods" in results[0].page_content

if __name__ == '__main__':
    test_vector_store()
    print("✓ Task 12 passed!")
