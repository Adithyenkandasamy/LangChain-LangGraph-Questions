import os

hour_dir = "practical/hour_7"
os.makedirs(hour_dir, exist_ok=True)

tasks = [
    ("task_01_pdf_loader_simulation.py", "LC-H7-P01", "PDF Document Loader & Page Ingestion",
"""Implement a loader `PDFIngestionLoader(filepath)` that reads or parses document content,
returning a list of document objects containing `page_content` and `metadata` (e.g., page number and source).""",
r'''class Document:
    def __init__(self, page_content: str, metadata: dict = None):
        self.page_content = page_content
        self.metadata = metadata or {}

class PDFIngestionLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load(self, mock_pages=None) -> list:
        if mock_pages is None:
            mock_pages = [
                "LangGraph enables building robust stateful multi-agent workflows.",
                "Retrieval-Augmented Generation (RAG) augments LLMs with factual external knowledge.",
                "Tool calling enables agents to query vector databases dynamically."
            ]
        docs = []
        for idx, text in enumerate(mock_pages):
            docs.append(Document(page_content=text, metadata={"source": self.filepath, "page": idx + 1}))
        return docs

def test_pdf_loader():
    loader = PDFIngestionLoader("course_notes.pdf")
    docs = loader.load()
    assert len(docs) == 3
    assert docs[0].metadata["source"] == "course_notes.pdf"
    assert docs[0].metadata["page"] == 1
    assert "LangGraph" in docs[0].page_content

if __name__ == '__main__':
    test_pdf_loader()
    print("✓ Task 01 passed!")
'''),

    ("task_02_recursive_splitter_with_metadata.py", "LC-H7-P02", "Recursive Text Splitter with Chunk Metadata",
"""Implement `split_documents_with_metadata(documents, chunk_size=50, chunk_overlap=10)`
that splits long documents into smaller chunks while preserving and updating chunk metadata (`chunk_id`).""",
r'''class SimpleDoc:
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
'''),

    ("task_03_vector_store_retriever_tool.py", "LC-H7-P03", "Vector Store as an Executable Tool",
"""Implement a `create_retriever_tool(name, description, docs)` function that wraps
document similarity lookup into a callable tool with name, description, and execution signature.""",
r'''class VectorRetrieverTool:
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
'''),

    ("task_04_rag_agent_state_schema.py", "LC-H7-P04", "RAG Agent State Schema with Reducer",
"""Define `AgentState` schema dictionary structure with `messages`, `retrieved_docs`,
and a reducer function `messages_reducer(existing, new_messages)` that appends messages.""",
r'''def messages_reducer(existing: list, new_messages: list) -> list:
    combined = list(existing)
    for msg in new_messages:
        combined.append(msg)
    return combined

def create_initial_state(user_query: str) -> dict:
    return {
        "messages": [{"role": "user", "content": user_query}],
        "retrieved_docs": [],
        "iterations": 0,
        "is_complete": False
    }

def test_state_schema():
    s = create_initial_state("What is LangGraph?")
    assert s["iterations"] == 0
    assert len(s["messages"]) == 1
    updated_messages = messages_reducer(s["messages"], [{"role": "assistant", "content": "LangGraph is stateful."}])
    assert len(updated_messages) == 2

if __name__ == '__main__':
    test_state_schema()
    print("✓ Task 04 passed!")
'''),

    ("task_05_mock_llm_with_tool_binding.py", "LC-H7-P05", "LLM Tool Binding & Decision Emulator",
"""Implement a mock chat model class `BindableMockLLM` with `.bind_tools(tools)` and `.invoke(messages)`.
If a tool matches the user query keywords, the mock LLM outputs a tool call; otherwise it returns a direct response.""",
r'''class BindableMockLLM:
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
'''),

    ("task_06_tool_execution_node.py", "LC-H7-P06", "LangGraph Tool Execution Node",
"""Implement `execute_tool_node(state, tools_map)` that extracts tool calls from the last
assistant message, executes the matching tool, and appends a `tool` role message to state.""",
r'''def execute_tool_node(state: dict, tools_map: dict) -> dict:
    messages = state["messages"]
    last_msg = messages[-1]
    tool_calls = last_msg.get("tool_calls", [])

    new_messages = []
    for tc in tool_calls:
        tool_name = tc.get("name")
        args = tc.get("args", {})
        if tool_name in tools_map:
            tool_fn = tools_map[tool_name]
            result = tool_fn(**args)
        else:
            result = f"Error: Tool {tool_name} not found."
        new_messages.append({"role": "tool", "name": tool_name, "content": result})

    state["messages"].extend(new_messages)
    return state

def test_tool_node():
    tools = {"rag_search": lambda query: f"Retrieved docs for {query}"}
    state = {
        "messages": [
            {"role": "assistant", "tool_calls": [{"name": "rag_search", "args": {"query": "LangGraph"}}]}
        ]
    }
    updated = execute_tool_node(state, tools)
    assert len(updated["messages"]) == 2
    assert updated["messages"][-1]["role"] == "tool"
    assert "Retrieved docs" in updated["messages"][-1]["content"]

if __name__ == '__main__':
    test_tool_node()
    print("✓ Task 06 passed!")
'''),

    ("task_07_rag_agent_router_edge.py", "LC-H7-P07", "RAG Agent Conditional Router Edge",
"""Implement `should_continue(state)` routing function:
If the last message contains `tool_calls`, return `'tools'`;
Otherwise, return `'end'`.""",
r'''def should_continue(state: dict) -> str:
    messages = state.get("messages", [])
    if not messages:
        return "end"
    last_msg = messages[-1]
    tool_calls = last_msg.get("tool_calls")
    if tool_calls and len(tool_calls) > 0:
        return "tools"
    return "end"

def test_router():
    s1 = {"messages": [{"role": "assistant", "tool_calls": [{"name": "search"}]}]}
    assert should_continue(s1) == "tools"

    s2 = {"messages": [{"role": "assistant", "content": "All clear."}]}
    assert should_continue(s2) == "end"

if __name__ == '__main__':
    test_router()
    print("✓ Task 07 passed!")
'''),

    ("task_08_context_synthesizer_node.py", "LC-H7-P08", "Context Synthesis & Final Response Node",
"""Implement `synthesize_answer_node(state)` that takes retrieved tool outputs and
formats a comprehensive synthesized answer citing the source context.""",
r'''def synthesize_answer_node(state: dict) -> dict:
    tool_msgs = [m for m in state.get("messages", []) if m.get("role") == "tool"]
    user_msgs = [m for m in state.get("messages", []) if m.get("role") == "user"]

    query = user_msgs[-1]["content"] if user_msgs else "unknown"
    if tool_msgs:
        context_parts = [m["content"] for m in tool_msgs]
        combined_context = " | ".join(context_parts)
        answer = f"Based on retrieved facts ({combined_context}), here is the answer for: {query}"
    else:
        answer = f"Direct response for: {query}"

    state["messages"].append({"role": "assistant", "content": answer})
    state["is_complete"] = True
    return state

def test_synthesizer():
    state = {
        "messages": [
            {"role": "user", "content": "Explain LangGraph"},
            {"role": "tool", "content": "LangGraph is stateful"}
        ],
        "is_complete": False
    }
    updated = synthesize_answer_node(state)
    assert updated["is_complete"] is True
    assert "Based on retrieved facts" in updated["messages"][-1]["content"]

if __name__ == '__main__':
    test_synthesizer()
    print("✓ Task 08 passed!")
'''),

    ("task_09_agent_memory_buffer.py", "LC-H7-P09", "Multi-Turn Conversation Memory Window",
"""Implement a `ConversationWindowMemory(k=4)` that retains only the last `k` messages
to prevent token overflow while maintaining the initial system prompt.""",
r'''class ConversationWindowMemory:
    def __init__(self, k: int = 4):
        self.k = k

    def trim(self, messages: list) -> list:
        if len(messages) <= self.k:
            return list(messages)
        system_msgs = [m for m in messages if m.get("role") == "system"]
        non_system = [m for m in messages if m.get("role") != "system"]
        trimmed_non_system = non_system[-self.k:]
        return system_msgs + trimmed_non_system

def test_memory_trim():
    mem = ConversationWindowMemory(k=3)
    msgs = [
        {"role": "system", "content": "You are assistant"},
        {"role": "user", "content": "1"},
        {"role": "assistant", "content": "2"},
        {"role": "user", "content": "3"},
        {"role": "assistant", "content": "4"}
    ]
    res = mem.trim(msgs)
    assert len(res) == 4  # 1 system + last 3 messages
    assert res[0]["role"] == "system"
    assert res[-1]["content"] == "4"

if __name__ == '__main__':
    test_memory_trim()
    print("✓ Task 09 passed!")
'''),

    ("task_10_empty_retrieval_fallback.py", "LC-H7-P10", "Empty Retrieval Guard & Fallback Handler",
"""Implement a fallback handler `handle_empty_retrieval(state)`:
If the retriever returns no content or indicates failure, set state flag `fallback_used=True`
and generate a courteous notice that external data was unavailable.""",
r'''def handle_empty_retrieval(state: dict) -> dict:
    last_msg = state["messages"][-1]
    if last_msg.get("role") == "tool" and ("no relevant" in last_msg.get("content", "").lower() or not last_msg.get("content")):
        state["fallback_used"] = True
        state["messages"].append({
            "role": "assistant",
            "content": "I could not find relevant documentation in the knowledge base. Answering from general knowledge."
        })
    else:
        state["fallback_used"] = False
    return state

def test_fallback():
    s1 = {"messages": [{"role": "tool", "content": "No relevant context found."}]}
    res1 = handle_empty_retrieval(s1)
    assert res1["fallback_used"] is True
    assert "could not find" in res1["messages"][-1]["content"]

    s2 = {"messages": [{"role": "tool", "content": "Found section 4.2"}]}
    res2 = handle_empty_retrieval(s2)
    assert res2["fallback_used"] is False

if __name__ == '__main__':
    test_fallback()
    print("✓ Task 10 passed!")
'''),

    ("task_11_human_in_the_loop_review.py", "LC-H7-P11", "Human-in-the-Loop Verification Intercept",
"""Implement `human_verification_intercept(state, user_approval=True, correction=None)`
that allows human intervention before saving or finalizing an action.""",
r'''def human_verification_intercept(state: dict, user_approval: bool = True, correction: str = None) -> dict:
    if user_approval:
        state["approval_status"] = "APPROVED"
    else:
        state["approval_status"] = "REJECTED"
        if correction:
            state["messages"].append({"role": "human_feedback", "content": correction})
    return state

def test_human_intercept():
    s = {"messages": [{"role": "assistant", "content": "Drafting contract..."}]}
    res_app = human_verification_intercept(s, user_approval=True)
    assert res_app["approval_status"] == "APPROVED"

    res_rej = human_verification_intercept(s, user_approval=False, correction="Adjust clause 3")
    assert res_rej["approval_status"] == "REJECTED"
    assert res_rej["messages"][-1]["content"] == "Adjust clause 3"

if __name__ == '__main__':
    test_human_intercept()
    print("✓ Task 11 passed!")
'''),

    ("task_12_graph_snapshot_inspector.py", "LC-H7-P12", "LangGraph State Snapshot Inspector",
"""Implement `StateSnapshotManager` that logs state snapshots at each node execution
and provides a method `get_snapshot(step_index)` and `diff(idx1, idx2)`.""",
r'''import copy

class StateSnapshotManager:
    def __init__(self):
        self.snapshots = []

    def record_step(self, node_name: str, state: dict):
        self.snapshots.append({
            "step": len(self.snapshots),
            "node": node_name,
            "state": copy.deepcopy(state)
        })

    def get_snapshot(self, idx: int) -> dict:
        return self.snapshots[idx]

    def diff_keys(self, idx1: int, idx2: int) -> list:
        s1 = self.snapshots[idx1]["state"]
        s2 = self.snapshots[idx2]["state"]
        changed = []
        for k in set(s1.keys()).union(s2.keys()):
            if s1.get(k) != s2.get(k):
                changed.append(k)
        return changed

def test_snapshots():
    sm = StateSnapshotManager()
    sm.record_step("start", {"step": 0, "status": "init"})
    sm.record_step("agent", {"step": 1, "status": "working"})
    assert len(sm.snapshots) == 2
    diff = sm.diff_keys(0, 1)
    assert "step" in diff and "status" in diff

if __name__ == '__main__':
    test_snapshots()
    print("✓ Task 12 passed!")
'''),

    ("task_13_max_recursion_guard.py", "LC-H7-P13", "Agent Graph Max Recursion Guard",
"""Implement `GraphRecursionGuard(max_depth=10)` class that tracks graph node transitions
and raises a `RecursionError` if transitions exceed `max_depth`.""",
r'''class GraphRecursionGuard:
    def __init__(self, max_depth: int = 10):
        self.max_depth = max_depth
        self.current_depth = 0

    def step(self, node_name: str):
        self.current_depth += 1
        if self.current_depth > self.max_depth:
            raise RecursionError(f"Maximum graph recursion depth ({self.max_depth}) exceeded at node '{node_name}'.")

    def reset(self):
        self.current_depth = 0

def test_recursion_guard():
    guard = GraphRecursionGuard(max_depth=3)
    guard.step("node_1")
    guard.step("node_2")
    guard.step("node_1")
    try:
        guard.step("node_2")
        assert False, "Should have raised RecursionError"
    except RecursionError as e:
        assert "depth (3) exceeded" in str(e)

if __name__ == '__main__':
    test_recursion_guard()
    print("✓ Task 13 passed!")
'''),

    ("task_14_streaming_event_parser.py", "LC-H7-P14", "Agent Graph Streaming Event Streamer",
"""Implement `parse_agent_events(events)` generator that categorizes events into
`node_start`, `tool_call`, `token`, and `node_end`.""",
r'''def parse_agent_events(events: list):
    parsed = []
    for ev in events:
        ev_type = ev.get("event")
        if ev_type == "on_chat_model_stream":
            parsed.append({"type": "token", "data": ev.get("data", {}).get("chunk", "")})
        elif ev_type == "on_tool_start":
            parsed.append({"type": "tool_call", "tool": ev.get("name")})
        elif ev_type == "on_chain_end":
            parsed.append({"type": "node_end", "output": ev.get("data", {}).get("output")})
    return parsed

def test_event_parser():
    raw_events = [
        {"event": "on_tool_start", "name": "vector_search"},
        {"event": "on_chat_model_stream", "data": {"chunk": "Hello"}},
        {"event": "on_chain_end", "data": {"output": "Done"}}
    ]
    parsed = parse_agent_events(raw_events)
    assert len(parsed) == 3
    assert parsed[0]["type"] == "tool_call"
    assert parsed[1]["type"] == "token"
    assert parsed[2]["type"] == "node_end"

if __name__ == '__main__':
    test_event_parser()
    print("✓ Task 14 passed!")
'''),

    ("task_15_autonomous_rag_agent.py", "LC-H7-P15", "Complete End-to-End Autonomous RAG Agent",
"""Implement a complete autonomous RAG agent class `AutonomousRAGAgent(docs)` that coordinates:
1. Agent node: calls LLM with tool binding
2. Router: checks for tool call
3. Tool execution node: queries vector store and returns context
4. Synthesizer node: produces final answer with verified facts
5. Complete execution loop with assertion test suite.""",
r'''class AutonomousRAGAgent:
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
''')
]

catalog_lines = [
    "# Hour 7 Practical Challenges Catalog",
    "",
    "Tier: **Mastery** | Focus: `Autonomous LangGraph RAG Agent, Ingestion & Tool Nodes`",
    "",
    "| ID | Task Title | Difficulty | File Link |",
    "| :---: | :--- | :---: | :--- |"
]

for filename, task_id, title, desc, code in tasks:
    filepath = os.path.join(hour_dir, filename)
    content = f'''"""
PRACTICAL CHALLENGE: {title} ({task_id})
=====================================================
ID: {task_id}
Curriculum Tier: Mastery | Focus: Autonomous LangGraph RAG Agent
Task:
{desc.strip()}

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
{code.strip()}
'''
    with open(filepath, "w") as f:
        f.write(content)
    
    catalog_lines.append(f"| `{task_id}` | {title} | `Mastery` | [{filename}]({filename}) |")

catalog_path = os.path.join(hour_dir, "README.md")
with open(catalog_path, "w") as f:
    f.write("\n".join(catalog_lines) + "\n")

print("Generated Hour 7 practical tasks successfully via Python.")
