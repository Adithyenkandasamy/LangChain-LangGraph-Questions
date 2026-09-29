"""
PRACTICAL CHALLENGE: LLM Tool Binding & Decision Emulator (LC-H7-P05)
=====================================================
ID: LC-H7-P05
Curriculum Tier: Mastery | Focus: Autonomous LangGraph RAG Agent
Task:
Implement a mock chat model class `BindableMockLLM` with `.bind_tools(tools)` and `.invoke(messages)`.
If a tool matches the user query keywords, the mock LLM outputs a tool call; otherwise it returns a direct response.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class BindableMockLLM:
    def __init__(self, system_knowledge: dict = None):
        self.system_knowledge = system_knowledge or {}
        self.bound_tools = []

    def bind_tools(self, tools: list):
        self.bound_tools = tools
        return self

    def invoke(self, messages: list) -> dict:
        last_msg = messages[-1]
        content = last_msg.get("content", "").lower()

        # Check if query requires retrieval
        for tool in self.bound_tools:
            if "lookup" in tool or "search" in tool or "knowledge" in tool:
                if any(w in content for w in ["what", "how", "explain", "who", "where"]):
                    return {
                        "role": "assistant",
                        "content": None,
                        "tool_calls": [{"name": tool, "args": {"query": last_msg.get("content")}}]
                    }
        return {"role": "assistant", "content": f"Answered directly: {last_msg.get('content')}", "tool_calls": []}

def test_bind_tools():
    llm = BindableMockLLM().bind_tools(["rag_lookup"])
    res1 = llm.invoke([{"role": "user", "content": "What is Chroma?"}])
    assert len(res1["tool_calls"]) == 1
    assert res1["tool_calls"][0]["name"] == "rag_lookup"

    res2 = llm.invoke([{"role": "user", "content": "Hello!"}])
    assert len(res2["tool_calls"]) == 0
    assert "Answered directly" in res2["content"]

if __name__ == '__main__':
    test_bind_tools()
    print("✓ Task 05 passed!")
