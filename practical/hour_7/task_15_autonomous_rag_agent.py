"""
PRACTICAL CHALLENGE: Complete End-to-End Autonomous RAG Agent (LC-H7-P15)
=====================================================
ID: LC-H7-P15
Curriculum Tier: Mastery | Focus: Autonomous LangGraph RAG Agent
Task:
Implement a complete autonomous RAG agent class `AutonomousRAGAgent(docs)` that coordinates:
1. Agent node: calls LLM with tool binding
2. Router: checks for tool call
3. Tool execution node: queries vector store and returns context
4. Synthesizer node: produces final answer with verified facts
5. Complete execution loop with assertion test suite.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class AutonomousRAGAgent:
    def __init__(self, knowledge_base: list):
        self.kb = knowledge_base

    def retrieve(self, query: str) -> str:
        q_tokens = set(query.lower().split())
        matched = [doc for doc in self.kb if any(t in doc.lower() for t in q_tokens)]
        return " | ".join(matched) if matched else "No info found."

    def run(self, user_query: str) -> dict:
        state = {
            "query": user_query,
            "retrieved_context": None,
            "final_answer": None,
            "steps": []
        }
        
        # Step 1: Agent reasoning & tool request
        state["steps"].append("agent_think")
        if any(w in user_query.lower() for w in ["what", "how", "tell", "explain"]):
            # Step 2: Tool execution
            state["steps"].append("tool_retrieval")
            context = self.retrieve(user_query)
            state["retrieved_context"] = context
        
        # Step 3: Synthesis
        state["steps"].append("synthesizer")
        if state["retrieved_context"]:
            state["final_answer"] = f"Verified: {state['retrieved_context']}"
        else:
            state["final_answer"] = f"Direct answer to: {user_query}"
        
        return state

def test_full_rag_agent():
    kb = [
        "LangGraph supports cyclic and stateful multi-agent workflows.",
        "Chroma vector store indexes chunks using dense embeddings."
    ]
    agent = AutonomousRAGAgent(kb)
    res = agent.run("What does LangGraph support?")
    assert "agent_think" in res["steps"]
    assert "tool_retrieval" in res["steps"]
    assert "synthesizer" in res["steps"]
    assert "cyclic and stateful" in res["final_answer"]

    direct_res = agent.run("Greetings")
    assert "tool_retrieval" not in direct_res["steps"]
    assert "Direct answer" in direct_res["final_answer"]

if __name__ == '__main__':
    test_full_rag_agent()
    print("✓ Task 15 passed!")
