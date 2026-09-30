"""
PRACTICAL CHALLENGE: Metadata Filtering in Vector Search (LC-H3-P14)
=====================================================
ID: LC-H3-P14
Curriculum Tier: Intermediate | Focus: Document Ingestion & Vector Storage
Task:
Extend similarity search to accept a `filter_dict` parameter that restricts candidate documents
to those whose metadata matches all specified key-value constraints.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
from task_12_in_memory_vector_store import InMemoryVectorStore, Document
from task_11_cosine_similarity import cosine_similarity

class FilterableVectorStore(InMemoryVectorStore):
    def similarity_search_with_filter(self, query: str, filter_dict: dict, k: int = 2) -> list:
        q_vec = self.embedding_model.embed_query(query)
        scored = []
        for rec in self.records:
            doc = rec["doc"]
            # verify match
            match = all(doc.metadata.get(k) == v for k, v in filter_dict.items())
            if match:
                score = cosine_similarity(q_vec, rec["vector"])
                scored.append((score, doc))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [doc for score, doc in scored[:k]]

def test_metadata_filtering():
    store = FilterableVectorStore()
    docs = [
        Document("LangChain tutorial part 1", {"topic": "langchain", "version": 1}),
        Document("LangChain tutorial part 2", {"topic": "langchain", "version": 2}),
        Document("General python guide", {"topic": "python", "version": 1})
    ]
    store.add_documents(docs)

    res = store.similarity_search_with_filter("tutorial", filter_dict={"version": 2}, k=5)
    assert len(res) == 1
    assert res[0].metadata["version"] == 2

if __name__ == '__main__':
    test_metadata_filtering()
    print("✓ Task 14 passed!")
