"""
PRACTICAL CHALLENGE: Vector Store as an Executable Tool (LC-H7-P03)
=====================================================
ID: LC-H7-P03
Curriculum Tier: Mastery | Focus: Autonomous LangGraph RAG Agent
Task:
Implement a `create_retriever_tool(name, description, docs)` function that wraps
document similarity lookup into a callable tool with name, description, and execution signature.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class VectorRetrieverTool:
    def __init__(self, name: str, description: str, docs: list):
        self.name = name
        self.description = description
        self.docs = docs

    def run(self, query: str, top_k: int = 2) -> str:
        q_tokens = set(query.lower().split())
        scored = []
        for d in self.docs:
            d_tokens = set(d.lower().split())
            overlap = len(q_tokens.intersection(d_tokens))
            scored.append((overlap, d))
        scored.sort(key=lambda x: x[0], reverse=True)
        results = [doc for score, doc in scored[:top_k] if score > 0]
        if not results:
            return "No relevant context found."
        return "\n---\n".join(results)

def create_retriever_tool(name: str, description: str, docs: list) -> VectorRetrieverTool:
    return VectorRetrieverTool(name, description, docs)

def test_retriever_tool():
    docs = [
        "LangGraph uses state graphs with nodes and edges.",
        "LangChain standardizes model invocation and prompt templates.",
        "Chroma is an open-source vector database."
    ]
    tool = create_retriever_tool("rag_lookup", "Search knowledge base", docs)
    res = tool.run("tell me about Chroma database")
    assert "vector database" in res

if __name__ == '__main__':
    test_retriever_tool()
    print("✓ Task 03 passed!")
