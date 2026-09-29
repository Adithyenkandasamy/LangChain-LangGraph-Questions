import os

hour_dir = "practical/hour_6"
os.makedirs(hour_dir, exist_ok=True)

tasks = [
    ("task_01_router_node.py", "LC-H6-P01", "Dynamic Router Node Implementation",
"""Implement a router node function `decide_next_node(state)` that inspects the last message
in `state["messages"]`. If the message indicates a tool call, route to 'tool_node'; if it says 'done' or 'save', route to 'end'; otherwise route to 'agent'.""",
r'''def decide_next_node(state: dict) -> str:
    messages = state.get("messages", [])
    if not messages:
        return "agent"
    last_msg = messages[-1]
    if isinstance(last_msg, dict):
        if last_msg.get("tool_calls"):
            return "tool_node"
        content = last_msg.get("content", "").lower()
    else:
        content = getattr(last_msg, "content", "").lower()

    if "save" in content or "done" in content or "exit" in content:
        return "end"
    return "agent"

def test_router_node():
    assert decide_next_node({"messages": []}) == "agent"
    assert decide_next_node({"messages": [{"tool_calls": ["c1"]}]}) == "tool_node"
    assert decide_next_node({"messages": [{"content": "All done, please save."}]}) == "end"
    assert decide_next_node({"messages": [{"content": "Please rewrite the intro."}]}) == "agent"

if __name__ == '__main__':
    test_router_node()
    print("✓ Task 01 passed!")
'''),

    ("task_02_loop_counter_safeguard.py", "LC-H6-P02", "Maximum Iteration Loop Safeguard",
"""Implement a guard function `check_iteration_limit(state, max_iterations=5)` that increments
`state['loop_count']` and returns True if loop should continue, or raises/returns False if limit is exceeded.""",
r'''def check_iteration_limit(state: dict, max_iterations: int = 5) -> bool:
    count = state.get("loop_count", 0) + 1
    state["loop_count"] = count
    if count > max_iterations:
        state["status"] = "MAX_ITERATIONS_REACHED"
        return False
    return True

def test_loop_counter():
    state = {"loop_count": 0}
    for _ in range(5):
        assert check_iteration_limit(state, max_iterations=5) is True
    
    # 6th iteration hits limit
    assert check_iteration_limit(state, max_iterations=5) is False
    assert state["status"] == "MAX_ITERATIONS_REACHED"

if __name__ == '__main__':
    test_loop_counter()
    print("✓ Task 02 passed!")
'''),

    ("task_03_number_guessing_loop.py", "LC-H6-P03", "Iterative Loop State Simulation",
"""Simulate the iterative number guessing loop demonstrated in the lecture:
An agent makes a guess, state receives feedback ('higher' or 'lower'), updates bounds, and repeats until guessed.""",
r'''def simulate_binary_search_loop(target: int, low: int = 1, high: int = 100) -> list:
    history = []
    guess = (low + high) // 2
    while low <= high:
        history.append(guess)
        if guess == target:
            break
        elif guess < target:
            low = guess + 1
        else:
            high = guess - 1
        guess = (low + high) // 2
    return history

def test_number_guessing():
    target = 42
    guesses = simulate_binary_search_loop(target, low=1, high=100)
    assert guesses[-1] == 42
    assert len(guesses) <= 7  # log2(100) < 7

if __name__ == '__main__':
    test_number_guessing()
    print("✓ Task 03 passed!")
'''),

    ("task_04_langgraph_tool_node.py", "LC-H6-P04", "LangGraph ToolNode Execution Pattern",
"""Implement a `ToolNode` class that executes tool calls from the state's latest message
and returns updated state with appended tool messages.""",
r'''class ToolNode:
    def __init__(self, tools_dict: dict):
        self.tools = tools_dict

    def invoke(self, state: dict) -> dict:
        messages = list(state.get("messages", []))
        last_msg = messages[-1]
        tool_calls = last_msg.get("tool_calls", [])

        new_tool_messages = []
        for call in tool_calls:
            fn = self.tools.get(call["name"])
            if fn:
                res = fn(**call["args"])
            else:
                res = f"Tool {call['name']} not found"
            new_tool_messages.append({"role": "tool", "content": str(res), "id": call["id"]})

        messages.extend(new_tool_messages)
        return {"messages": messages}

def test_tool_node():
    node = ToolNode({"calc": lambda x: x * 10})
    state = {
        "messages": [
            {"role": "ai", "tool_calls": [{"name": "calc", "args": {"x": 5}, "id": "call_10"}]}
        ]
    }
    updated = node.invoke(state)
    assert len(updated["messages"]) == 2
    assert updated["messages"][1]["role"] == "tool"
    assert updated["messages"][1]["content"] == "50"

if __name__ == '__main__':
    test_tool_node()
    print("✓ Task 04 passed!")
'''),

    ("task_05_document_state_schema.py", "LC-H6-P05", "Document Crafter State Schema",
"""Define a Document Crafter State schema containing:
- `messages`: list of conversation messages
- `document_content`: current draft string
- `revision_count`: integer tracking revisions.""",
r'''from typing import TypedDict, List

class DocumentCrafterState(TypedDict):
    messages: List[dict]
    document_content: str
    revision_count: int

def init_document_state(prompt: str) -> DocumentCrafterState:
    return {
        "messages": [{"role": "user", "content": prompt}],
        "document_content": "",
        "revision_count": 0
    }

def test_document_state():
    state = init_document_state("Draft a leave application")
    assert state["document_content"] == ""
    assert state["revision_count"] == 0
    assert len(state["messages"]) == 1

if __name__ == '__main__':
    test_document_state()
    print("✓ Task 05 passed!")
'''),

    ("task_06_document_create_node.py", "LC-H6-P06", "Document Creation Node",
"""Implement a `create_document_node(state)` that generates initial document content
from the user's prompt and sets `revision_count` to 1.""",
r'''def create_document_node(state: dict) -> dict:
    user_prompt = state["messages"][-1]["content"]
    draft = f"Subject: Official Notice\n\nDear Team,\n\nRegarding: {user_prompt}\n\nSincerely,\nManagement"
    return {
        "document_content": draft,
        "revision_count": 1,
        "messages": state["messages"] + [{"role": "ai", "content": "Draft created successfully."}]
    }

def test_create_document_node():
    initial = {"messages": [{"role": "user", "content": "Holiday Schedule"}], "revision_count": 0}
    result = create_document_node(initial)

    assert result["revision_count"] == 1
    assert "Regarding: Holiday Schedule" in result["document_content"]
    assert len(result["messages"]) == 2

if __name__ == '__main__':
    test_create_document_node()
    print("✓ Task 06 passed!")
'''),

    ("task_07_document_update_node.py", "LC-H6-P07", "Document Revision & Update Node",
"""Implement `update_document_node(state, instruction)` that modifies existing `document_content`,
increments `revision_count`, and appends a revision note.""",
r'''def update_document_node(state: dict, instruction: str) -> dict:
    current = state.get("document_content", "")
    updated_content = current + f"\n\n[Revision note: {instruction}]"
    revisions = state.get("revision_count", 0) + 1
    return {
        "document_content": updated_content,
        "revision_count": revisions,
        "messages": state.get("messages", []) + [{"role": "ai", "content": f"Updated for: {instruction}"}]
    }

def test_update_document_node():
    base_state = {
        "document_content": "Base Content",
        "revision_count": 1,
        "messages": []
    }
    updated = update_document_node(base_state, "Add contact phone number")

    assert updated["revision_count"] == 2
    assert "[Revision note: Add contact phone number]" in updated["document_content"]

if __name__ == '__main__':
    test_update_document_node()
    print("✓ Task 07 passed!")
'''),

    ("task_08_document_save_node.py", "LC-H6-P08", "Document Persistence Node",
"""Implement `save_document_node(state, filename)` that simulates writing `document_content`
to a target file and marks state with `status='SAVED'`.""",
r'''def save_document_node(state: dict, filename: str) -> dict:
    content = state.get("document_content", "")
    if not content.strip():
        raise ValueError("Cannot save empty document content.")
    
    # In real app writes to disk; here sets metadata
    return {
        "saved_filename": filename,
        "status": "SAVED",
        "file_size_bytes": len(content.encode("utf-8")),
        "messages": state.get("messages", []) + [{"role": "system", "content": f"Document saved as {filename}"}]
    }

def test_save_document_node():
    state = {"document_content": "Important business memorandum text.", "messages": []}
    res = save_document_node(state, "memo.txt")

    assert res["status"] == "SAVED"
    assert res["saved_filename"] == "memo.txt"
    assert res["file_size_bytes"] > 0

    try:
        save_document_node({"document_content": "   "}, "memo.txt")
        assert False, "Should raise ValueError on empty content"
    except ValueError:
        pass

if __name__ == '__main__':
    test_save_document_node()
    print("✓ Task 08 passed!")
'''),

    ("task_09_message_formatter_helper.py", "LC-H6-P09", "Message Pretty-Printer Utility",
"""Implement `print_messages(messages)` from the lecture that formats human, AI, and tool
messages with clear visual delimiters and color tags.""",
r'''def format_message_display(msg: dict) -> str:
    role = msg.get("role", "unknown").upper()
    content = msg.get("content", "")
    if "tool_calls" in msg and msg["tool_calls"]:
        calls = ", ".join([c.get("name", "") for c in msg["tool_calls"]])
        return f"[{role}] -> ToolCall: {calls}"
    return f"[{role}]: {content}"

def print_messages(messages: list) -> str:
    if not messages:
        return "No messages."
    lines = [format_message_display(m) for m in messages]
    return "\n---\n".join(lines)

def test_print_messages():
    msgs = [
        {"role": "user", "content": "Need an email draft"},
        {"role": "ai", "content": "Here is the draft"},
        {"role": "ai", "tool_calls": [{"name": "save_file"}]}
    ]
    formatted = print_messages(msgs)
    assert "[USER]: Need an email draft" in formatted
    assert "[AI]: Here is the draft" in formatted
    assert "[AI] -> ToolCall: save_file" in formatted

if __name__ == '__main__':
    test_print_messages()
    print("✓ Task 09 passed!")
'''),

    ("task_10_human_in_the_loop_simulation.py", "LC-H6-P10", "Simulating Human Review Interruption",
"""Implement a review handler `human_review_step(state, approved=True, feedback='')` that either
routes to save if approved, or loops back to update node with human feedback.""",
r'''def human_review_step(state: dict, approved: bool, feedback: str = "") -> dict:
    if approved:
        return {"next_step": "save", "review_status": "APPROVED"}
    else:
        return {
            "next_step": "update",
            "review_status": "REVISE",
            "messages": state.get("messages", []) + [{"role": "user", "content": f"Please revise: {feedback}"}]
        }

def test_human_review():
    state = {"messages": [{"role": "ai", "content": "Draft v1"}]}
    
    # User rejects draft with feedback
    rev = human_review_step(state, approved=False, feedback="Tone is too casual")
    assert rev["next_step"] == "update"
    assert "Tone is too casual" in rev["messages"][-1]["content"]

    # User approves
    app = human_review_step(state, approved=True)
    assert app["next_step"] == "save"
    assert app["review_status"] == "APPROVED"

if __name__ == '__main__':
    test_human_review()
    print("✓ Task 10 passed!")
'''),

    ("task_11_state_history_accumulator.py", "LC-H6-P11", "Preserving State Snapshots Across Iterations",
"""Implement a `StateCheckpointManager` that records a snapshot of the graph state at each iteration,
enabling history rollback and step debugging.""",
r'''import copy

class StateCheckpointManager:
    def __init__(self):
        self.checkpoints = []

    def save_checkpoint(self, step_name: str, state: dict):
        self.checkpoints.append({
            "step": step_name,
            "state": copy.deepcopy(state)
        })

    def get_step_state(self, step_idx: int) -> dict:
        return self.checkpoints[step_idx]["state"]

    def rollback_to_step(self, step_idx: int) -> dict:
        target = copy.deepcopy(self.checkpoints[step_idx]["state"])
        self.checkpoints = self.checkpoints[:step_idx + 1]
        return target

def test_checkpoints():
    mgr = StateCheckpointManager()
    state = {"count": 1}
    mgr.save_checkpoint("start", state)

    state["count"] = 2
    mgr.save_checkpoint("after_step1", state)

    state["count"] = 3
    mgr.save_checkpoint("after_step2", state)

    assert len(mgr.checkpoints) == 3
    rolled = mgr.rollback_to_step(1)
    assert rolled["count"] == 2
    assert len(mgr.checkpoints) == 2

if __name__ == '__main__':
    test_checkpoints()
    print("✓ Task 11 passed!")
'''),

    ("task_12_intent_detection_router.py", "LC-H6-P12", "Multi-Intent Classifier in LangGraph",
"""Implement an intent classifier `classify_document_action(user_text)` that categorizes
input into `['CREATE', 'UPDATE', 'SAVE', 'QUERY', 'UNKNOWN']`.""",
r'''def classify_document_action(text: str) -> str:
    low = text.lower()
    if any(k in low for k in ["save", "export", "download", "write to file"]):
        return "SAVE"
    if any(k in low for k in ["update", "modify", "change", "rewrite", "add"]):
        return "UPDATE"
    if any(k in low for k in ["create", "draft", "write me", "generate", "start"]):
        return "CREATE"
    if any(k in low for k in ["what", "show", "view", "read"]):
        return "QUERY"
    return "UNKNOWN"

def test_intent_detection():
    assert classify_document_action("Please draft a resignation letter") == "CREATE"
    assert classify_document_action("Change the notice period to 30 days") == "UPDATE"
    assert classify_document_action("Save document as resignation.txt") == "SAVE"
    assert classify_document_action("What is the current word count?") == "QUERY"
    assert classify_document_action("Random greeting") == "UNKNOWN"

if __name__ == '__main__':
    test_intent_detection()
    print("✓ Task 12 passed!")
'''),

    ("task_13_cycle_detection.py", "LC-H6-P13", "Detecting Repetitive Tool Calling Loops",
"""Implement `detect_tool_cycle(tool_history, max_consecutive=3)` that flags when the exact same
tool and argument signature is called repeatedly without progress.""",
r'''def detect_tool_cycle(history: list, max_consecutive: int = 3) -> bool:
    if len(history) < max_consecutive:
        return False
    recent = history[-max_consecutive:]
    first = recent[0]
    return all(item == first for item in recent)

def test_cycle_detection():
    call1 = {"name": "search", "query": "python"}
    call2 = {"name": "search", "query": "langgraph"}

    assert detect_tool_cycle([call1, call1], max_consecutive=3) is False
    assert detect_tool_cycle([call1, call1, call1], max_consecutive=3) is True
    assert detect_tool_cycle([call1, call2, call1], max_consecutive=3) is False

if __name__ == '__main__':
    test_cycle_detection()
    print("✓ Task 13 passed!")
'''),

    ("task_14_state_reset_utility.py", "LC-H6-P14", "State Reset & Garbage Collection",
"""Implement `reset_document_session(state, preserve_history=False)` that resets draft content
and iteration count while optionally archiving prior messages.""",
r'''def reset_document_session(state: dict, preserve_history: bool = False) -> dict:
    new_state = {
        "document_content": "",
        "revision_count": 0,
        "status": "INITIALIZED"
    }
    if preserve_history:
        new_state["archived_messages"] = list(state.get("messages", []))
        new_state["messages"] = []
    else:
        new_state["messages"] = []
    return new_state

def test_state_reset():
    active_state = {
        "document_content": "Old Draft",
        "revision_count": 4,
        "messages": [{"role": "user", "content": "draft 1"}]
    }

    fresh = reset_document_session(active_state, preserve_history=True)
    assert fresh["document_content"] == ""
    assert fresh["revision_count"] == 0
    assert len(fresh["archived_messages"]) == 1

if __name__ == '__main__':
    test_state_reset()
    print("✓ Task 14 passed!")
'''),

    ("task_15_document_agent_orchestrator.py", "LC-H6-P15", "Complete Document Crafter Agent Loop",
"""Assemble the complete Document Crafter loop:
1. Receives initial prompt -> Creates draft
2. Receives update commands -> Applies revisions
3. Receives save command -> Persists document and outputs final state.""",
r'''from task_06_document_create_node import create_document_node
from task_07_document_update_node import update_document_node
from task_08_document_save_node import save_document_node
from task_12_intent_detection_router import classify_document_action

class DocumentCrafterAgent:
    def __init__(self):
        self.state = {"messages": [], "document_content": "", "revision_count": 0}

    def process_input(self, user_text: str, filename: str = "output.txt") -> dict:
        self.state["messages"].append({"role": "user", "content": user_text})
        action = classify_document_action(user_text)

        if action == "CREATE":
            updates = create_document_node(self.state)
            self.state.update(updates)
        elif action == "UPDATE":
            updates = update_document_node(self.state, user_text)
            self.state.update(updates)
        elif action == "SAVE":
            updates = save_document_node(self.state, filename)
            self.state.update(updates)
        return self.state

def test_document_agent():
    agent = DocumentCrafterAgent()
    s1 = agent.process_input("Create a project proposal draft")
    assert s1["revision_count"] == 1
    assert "Regarding: Create a project proposal draft" in s1["document_content"]

    s2 = agent.process_input("Update timeline to 6 months")
    assert s2["revision_count"] == 2
    assert "timeline to 6 months" in s2["document_content"]

    s3 = agent.process_input("Save proposal to file", filename="proposal.txt")
    assert s3["status"] == "SAVED"
    assert s3["saved_filename"] == "proposal.txt"

if __name__ == '__main__':
    test_document_agent()
    print("✓ Task 15 passed!")
''')
]

catalog_lines = [
    "# Hour 6 Practical Challenges Catalog",
    "",
    "Tier: **Advanced** | Focus: `LangGraph Cyclic Loops, State Reducers & Document Agents`",
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
Curriculum Tier: Advanced | Focus: LangGraph Loops & Document Crafter Agent
Task:
{desc.strip()}

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
{code.strip()}
'''
    with open(filepath, "w") as f:
        f.write(content)
    
    catalog_lines.append(f"| `{task_id}` | {title} | `Advanced` | [{filename}]({filename}) |")

catalog_path = os.path.join(hour_dir, "README.md")
with open(catalog_path, "w") as f:
    f.write("\n".join(catalog_lines) + "\n")

print("Generated Hour 6 successfully via Python.")
