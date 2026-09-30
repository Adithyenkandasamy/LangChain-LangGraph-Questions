"""
PRACTICAL CHALLENGE: Wrapping a Retriever as a Tool (LC-H4-P14)
=====================================================
ID: LC-H4-P14
Curriculum Tier: Advanced | Focus: Advanced RAG & Tool Interfaces
Task:
Implement `create_retriever_tool(retriever, name, description)` that returns a callable Tool
accepting `{'query': str}` and returning concatenated retrieved documents.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class MockRetriever:
    def __init__(self, data: dict):
        self.data = data
    def invoke(self, query: str) -> list:
        return self.data.get(query.lower(), ["No matching information found."])

def create_retriever_tool(retriever, name: str, description: str):
    def retriever_tool(query: str) -> str:
        docs = retriever.invoke(query)
        return "\n\n".join(docs)
    
    retriever_tool.name = name
    retriever_tool.description = description
    return retriever_tool

def test_retriever_tool():
    retriever = MockRetriever({"stock report": ["Apple Inc Q3 Profit up 12%", "Tesla deliveries steady"]})
    tool = create_retriever_tool(retriever, "stock_search", "Look up financial reports")

    assert tool.name == "stock_search"
    res = tool("stock report")
    assert "Apple Inc Q3 Profit up 12%" in res

if __name__ == '__main__':
    test_retriever_tool()
    print("✓ Task 14 passed!")
