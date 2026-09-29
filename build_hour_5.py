import os

hour_dir = "practical/hour_5"
os.makedirs(hour_dir, exist_ok=True)

tasks = [
    ("task_01_tool_call_schema.py", "LC-H5-P01", "Tool Call Representation & Validation",
"""Implement a `ToolCall` dataclass or dictionary representation with fields `name` (str),
`args` (dict), and `id` (str). Validate that `id` is a non-empty string and `args` is a valid dict.""",
r'''from dataclasses import dataclass, field

@dataclass
class ToolCall:
    name: str
    args: dict
    id: str

    def __post_init__(self):
        if not self.name or not isinstance(self.name, str):
            raise ValueError("ToolCall name must be a non-empty string.")
        if not isinstance(self.args, dict):
            raise TypeError("ToolCall args must be a dictionary.")
        if not self.id or not isinstance(self.id, str):
            raise ValueError("ToolCall id must be a non-empty string.")

def test_tool_call():
    tc = ToolCall(name="add", args={"a": 5, "b": 10}, id="call_12345")
    assert tc.name == "add"
    assert tc.args["a"] == 5
    assert tc.id == "call_12345"

    try:
        ToolCall(name="add", args="invalid_args", id="call_1")
        assert False, "Should raise TypeError"
    except TypeError:
        pass

if __name__ == '__main__':
    test_tool_call()
    print("✓ Task 01 passed!")
'''),

    ("task_02_ai_message_with_tools.py", "LC-H5-P02", "AIMessage with tool_calls Attribute",
"""Implement an `AIMessage` class that supports both optional text `content` and optional `tool_calls` list.
Provide a helper property `.has_tool_calls` returning True if `tool_calls` contains at least one item.""",
r'''class AIMessage:
    def __init__(self, content: str = "", tool_calls: list = None):
        self.content = content
        self.tool_calls = tool_calls or []

    @property
    def has_tool_calls(self) -> bool:
        return len(self.tool_calls) > 0

def test_ai_message_with_tools():
    msg_plain = AIMessage(content="Hello world!")
    assert not msg_plain.has_tool_calls

    msg_with_call = AIMessage(
        content="",
        tool_calls=[{"name": "fetch_stock", "args": {"symbol": "AAPL"}, "id": "call_99"}]
    )
    assert msg_with_call.has_tool_calls
    assert msg_with_call.tool_calls[0]["name"] == "fetch_stock"

if __name__ == '__main__':
    test_ai_message_with_tools()
    print("✓ Task 02 passed!")
'''),

    ("task_03_tool_message.py", "LC-H5-P03", "ToolMessage Output Wrapper",
"""Implement `ToolMessage` storing `content` (str), `tool_call_id` (str), and `role='tool'`.
Validate that `tool_call_id` matches the originating call id.""",
r'''class ToolMessage:
    def __init__(self, content: str, tool_call_id: str):
        if not tool_call_id or not isinstance(tool_call_id, str):
            raise ValueError("tool_call_id must be provided.")
        self.content = str(content)
        self.tool_call_id = tool_call_id

    @property
    def role(self) -> str:
        return "tool"

def test_tool_message():
    t_msg = ToolMessage(content="Result: 42", tool_call_id="call_abc")
    assert t_msg.role == "tool"
    assert t_msg.content == "Result: 42"
    assert t_msg.tool_call_id == "call_abc"

    try:
        ToolMessage(content="fail", tool_call_id="")
        assert False, "Should raise ValueError for empty tool_call_id"
    except ValueError:
        pass

if __name__ == '__main__':
    test_tool_message()
    print("✓ Task 03 passed!")
'''),

    ("task_04_bind_tools_simulation.py", "LC-H5-P04", "Simulating model.bind_tools()",
"""Implement a `BindToolsModel` class that accepts a list of registered tools and simulates
deciding between a direct text answer and generating tool calls based on user input keywords.""",
r'''from task_02_ai_message_with_tools import AIMessage

class BindToolsModel:
    def __init__(self, tools: list):
        self.tools_by_name = {getattr(t, "name", t.__name__): t for t in tools}

    def invoke(self, messages: list) -> AIMessage:
        last_text = messages[-1].content.lower()
        if "add" in last_text:
            return AIMessage(tool_calls=[{"name": "add", "args": {"a": 20, "b": 30}, "id": "call_1"}])
        elif "multiply" in last_text:
            return AIMessage(tool_calls=[{"name": "multiply", "args": {"a": 4, "b": 5}, "id": "call_2"}])
        return AIMessage(content="I can answer general questions directly.")

def add(a: int, b: int) -> int: return a + b
def multiply(a: int, b: int) -> int: return a * b

class MockMsg:
    def __init__(self, c): self.content = c

def test_bind_tools_model():
    model = BindToolsModel([add, multiply])
    ai_res = model.invoke([MockMsg("Please add 20 and 30")])
    assert ai_res.has_tool_calls
    assert ai_res.tool_calls[0]["name"] == "add"

    ai_text = model.invoke([MockMsg("What is your purpose?")])
    assert not ai_text.has_tool_calls
    assert "general questions" in ai_text.content

if __name__ == '__main__':
    test_bind_tools_model()
    print("✓ Task 04 passed!")
'''),

    ("task_05_tool_dispatcher.py", "LC-H5-P05", "Tool Dispatcher & ToolMessage Generator",
"""Implement `dispatch_tool_calls(tool_calls, tools_map)` that executes each tool call
and returns a list of corresponding `ToolMessage` instances.""",
r'''from task_03_tool_message import ToolMessage

def dispatch_tool_calls(tool_calls: list, tools_map: dict) -> list:
    tool_messages = []
    for tc in tool_calls:
        name = tc["name"]
        call_id = tc["id"]
        args = tc.get("args", {})
        if name not in tools_map:
            out = f"Error: Tool '{name}' not found."
        else:
            try:
                fn = tools_map[name]
                out = str(fn(**args))
            except Exception as e:
                out = f"Execution error: {str(e)}"
        tool_messages.append(ToolMessage(content=out, tool_call_id=call_id))
    return tool_messages

def test_tool_dispatcher():
    tools = {
        "add": lambda a, b: a + b,
        "greet": lambda name: f"Hello, {name}!"
    }
    calls = [
        {"name": "add", "args": {"a": 10, "b": 15}, "id": "c1"},
        {"name": "greet", "args": {"name": "Bob"}, "id": "c2"}
    ]
    results = dispatch_tool_calls(calls, tools)

    assert len(results) == 2
    assert results[0].content == "25" and results[0].tool_call_id == "c1"
    assert results[1].content == "Hello, Bob!" and results[1].tool_call_id == "c2"

if __name__ == '__main__':
    test_tool_dispatcher()
    print("✓ Task 05 passed!")
'''),

    ("task_06_two_turn_tool_execution.py", "LC-H5-P06", "Two-Turn LLM Tool Execution Loop",
"""Implement a two-turn loop `run_tool_turn(history, model, tools_map)`:
Turn 1: Model returns tool call
Turn 2: Tool executes and adds ToolMessage, Model runs again to produce final natural language answer.""",
r'''from task_02_ai_message_with_tools import AIMessage
from task_03_tool_message import ToolMessage
from task_05_tool_dispatcher import dispatch_tool_calls

class MockTwoTurnModel:
    def invoke(self, history: list) -> AIMessage:
        # Check if last message is a ToolMessage
        if history and getattr(history[-1], "role", "") == "tool":
            return AIMessage(content=f"The answer is {history[-1].content}.")
        return AIMessage(tool_calls=[{"name": "calc", "args": {"x": 7, "y": 6}, "id": "call_calc_1"}])

def run_tool_turn(history: list, model, tools_map: dict) -> AIMessage:
    first_response = model.invoke(history)
    if not first_response.has_tool_calls:
        return first_response

    history.append(first_response)
    tool_msgs = dispatch_tool_calls(first_response.tool_calls, tools_map)
    history.extend(tool_msgs)

    final_response = model.invoke(history)
    history.append(final_response)
    return final_response

def test_two_turn_loop():
    tools = {"calc": lambda x, y: x * y}
    model = MockTwoTurnModel()
    history = []

    final_ans = run_tool_turn(history, model, tools)
    assert final_ans.content == "The answer is 42."
    assert len(history) == 3 # AIMessage(calls) + ToolMessage + AIMessage(final)

if __name__ == '__main__':
    test_two_turn_loop()
    print("✓ Task 06 passed!")
'''),

    ("task_07_agent_state_schema.py", "LC-H5-P07", "LangGraph AgentState Definition",
"""Define an `AgentState` schema using `TypedDict` containing `messages` (list of messages)
and `sender` (str) metadata.""",
r'''from typing import TypedDict, List, Any

class AgentState(TypedDict):
    messages: List[Any]
    sender: str

def create_initial_state(user_text: str) -> AgentState:
    return {
        "messages": [{"role": "user", "content": user_text}],
        "sender": "user"
    }

def test_agent_state():
    state = create_initial_state("Analyze stock performance")
    assert state["sender"] == "user"
    assert len(state["messages"]) == 1
    assert state["messages"][0]["content"] == "Analyze stock performance"

if __name__ == '__main__':
    test_agent_state()
    print("✓ Task 07 passed!")
'''),

    ("task_08_add_messages_reducer.py", "LC-H5-P08", "add_messages Reducer Logic",
"""Implement the `add_messages(existing_messages, new_messages)` reducer logic that appends
messages or updates an existing message if their IDs match.""",
r'''def add_messages(existing: list, new_msgs: list) -> list:
    result = list(existing)
    id_to_index = {m.get("id"): idx for idx, m in enumerate(result) if "id" in m}

    for msg in new_msgs:
        m_id = msg.get("id")
        if m_id and m_id in id_to_index:
            result[id_to_index[m_id]] = msg
        else:
            result.append(msg)
            if m_id:
                id_to_index[m_id] = len(result) - 1
    return result

def test_add_messages_reducer():
    base = [{"id": "1", "content": "Hello"}]
    # Append new message
    res1 = add_messages(base, [{"id": "2", "content": "Hi"}])
    assert len(res1) == 2

    # Update existing message with matching id
    res2 = add_messages(res1, [{"id": "1", "content": "Updated Hello"}])
    assert len(res2) == 2
    assert res2[0]["content"] == "Updated Hello"

if __name__ == '__main__':
    test_add_messages_reducer()
    print("✓ Task 08 passed!")
'''),

    ("task_09_state_graph_nodes.py", "LC-H5-P09", "Adding Nodes to StateGraph",
"""Implement a `StateGraph` builder that registers nodes `graph.add_node(name, func)`
and prevents registering duplicate node names.""",
r'''class StateGraph:
    def __init__(self, state_schema):
        self.state_schema = state_schema
        self.nodes = {}

    def add_node(self, name: str, func):
        if name in self.nodes:
            raise ValueError(f"Node '{name}' already exists in graph.")
        self.nodes[name] = func

def test_graph_nodes():
    graph = StateGraph(dict)
    graph.add_node("agent", lambda state: state)
    graph.add_node("tools", lambda state: state)

    assert "agent" in graph.nodes and "tools" in graph.nodes

    try:
        graph.add_node("agent", lambda state: state)
        assert False, "Should raise ValueError for duplicate node"
    except ValueError:
        pass

if __name__ == '__main__':
    test_graph_nodes()
    print("✓ Task 09 passed!")
'''),

    ("task_10_linear_edges.py", "LC-H5-P10", "Registering Linear Edges",
"""Implement `.add_edge(start_node, end_node)` on `StateGraph` and support special markers
`START` and `END`.""",
r'''START = "__start__"
END = "__end__"

class StateGraphWithEdges:
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def add_node(self, name: str):
        self.nodes.add(name)

    def add_edge(self, start: str, end: str):
        if start != START and start not in self.nodes:
            raise KeyError(f"Start node '{start}' not defined.")
        if end != END and end not in self.nodes:
            raise KeyError(f"End node '{end}' not defined.")
        self.edges.append((start, end))

def test_linear_edges():
    g = StateGraphWithEdges()
    g.add_node("llm")
    g.add_node("formatter")

    g.add_edge(START, "llm")
    g.add_edge("llm", "formatter")
    g.add_edge("formatter", END)

    assert (START, "llm") in g.edges
    assert ("formatter", END) in g.edges

if __name__ == '__main__':
    test_linear_edges()
    print("✓ Task 10 passed!")
'''),

    ("task_11_conditional_edges.py", "LC-H5-P11", "Conditional Edges Routing",
"""Implement `.add_conditional_edges(source, condition_fn, path_map)` that evaluates state
and maps condition return value to the next target node.""",
r'''class ConditionalGraphRouter:
    def __init__(self):
        self.conditional_edges = {}

    def add_conditional_edges(self, source: str, condition_fn, path_map: dict):
        self.conditional_edges[source] = (condition_fn, path_map)

    def route_next(self, source: str, state: dict) -> str:
        condition_fn, path_map = self.conditional_edges[source]
        decision = condition_fn(state)
        return path_map[decision]

def test_conditional_edges():
    router = ConditionalGraphRouter()
    
    def check_tools(state):
        return "has_tools" if state.get("tool_calls") else "finish"

    router.add_conditional_edges(
        "agent",
        check_tools,
        {"has_tools": "tools_node", "finish": "end_node"}
    )

    next_with_tools = router.route_next("agent", {"tool_calls": ["call1"]})
    assert next_with_tools == "tools_node"

    next_no_tools = router.route_next("agent", {"tool_calls": []})
    assert next_no_tools == "end_node"

if __name__ == '__main__':
    test_conditional_edges()
    print("✓ Task 11 passed!")
'''),

    ("task_12_compile_graph.py", "LC-H5-P12", "Compiling StateGraph to Executable App",
"""Implement `.compile()` on `StateGraph` returning a `CompiledGraph` instance
with an `.invoke(initial_state)` method that runs linear node steps.""",
r'''class CompiledGraph:
    def __init__(self, nodes: dict, execution_order: list):
        self.nodes = nodes
        self.execution_order = execution_order

    def invoke(self, state: dict) -> dict:
        current_state = dict(state)
        for node_name in self.execution_order:
            node_fn = self.nodes[node_name]
            updates = node_fn(current_state)
            current_state.update(updates)
        return current_state

def test_compile_graph():
    nodes = {
        "step_a": lambda s: {"val": s["val"] + 10},
        "step_b": lambda s: {"val": s["val"] * 2}
    }
    app = CompiledGraph(nodes, ["step_a", "step_b"])
    result = app.invoke({"val": 5})

    # (5 + 10) * 2 = 30
    assert result["val"] == 30

if __name__ == '__main__':
    test_compile_graph()
    print("✓ Task 12 passed!")
'''),

    ("task_13_state_immutability.py", "LC-H5-P13", "Safe State Immutability across Nodes",
"""Implement node wrappers that verify input state is not mutated in-place and state updates
are returned as new dictionaries.""",
r'''import copy

def safe_node_runner(node_fn, current_state: dict) -> dict:
    state_snapshot = copy.deepcopy(current_state)
    updates = node_fn(copy.deepcopy(current_state))
    # verify current_state was not modified
    if current_state != state_snapshot:
        raise RuntimeError("Node improperly modified state in-place!")
    
    new_state = dict(current_state)
    new_state.update(updates)
    return new_state

def well_behaved_node(state):
    return {"count": state.get("count", 0) + 1}

def test_safe_state_runner():
    initial = {"count": 10, "label": "demo"}
    updated = safe_node_runner(well_behaved_node, initial)
    assert updated["count"] == 11
    assert initial["count"] == 10

if __name__ == '__main__':
    test_safe_state_runner()
    print("✓ Task 13 passed!")
'''),

    ("task_14_multi_tool_call_resolution.py", "LC-H5-P14", "Simultaneous Multi-Tool Resolution",
"""Implement resolution of multiple tool calls issued in a single turn, preserving matching IDs
and collecting results into a single list of ToolMessages.""",
r'''from task_03_tool_message import ToolMessage

def resolve_multiple_calls(tool_calls: list, tool_registry: dict) -> list:
    out = []
    for tc in tool_calls:
        fn = tool_registry[tc["name"]]
        val = fn(**tc["args"])
        out.append(ToolMessage(content=str(val), tool_call_id=tc["id"]))
    return out

def test_multi_tool_resolution():
    registry = {
        "get_stock_price": lambda symbol: 150.0 if symbol == "AAPL" else 200.0,
        "get_pe_ratio": lambda symbol: 28.5
    }
    calls = [
        {"name": "get_stock_price", "args": {"symbol": "AAPL"}, "id": "c1"},
        {"name": "get_pe_ratio", "args": {"symbol": "AAPL"}, "id": "c2"}
    ]
    tool_messages = resolve_multiple_calls(calls, registry)

    assert len(tool_messages) == 2
    assert tool_messages[0].content == "150.0" and tool_messages[0].tool_call_id == "c1"
    assert tool_messages[1].content == "28.5" and tool_messages[1].tool_call_id == "c2"

if __name__ == '__main__':
    test_multi_tool_resolution()
    print("✓ Task 14 passed!")
'''),

    ("task_15_minimal_compiled_agent.py", "LC-H5-P15", "Minimal End-to-End StateGraph Agent",
"""Assemble a minimal compiled StateGraph with:
- Start -> 'agent_node' -> 'router'
- Router routes to 'tool_node' if tool call present, else END
- 'tool_node' routes back to 'agent_node'.""",
r'''class SimpleStateGraphAgent:
    def __init__(self, tool_func):
        self.tool_func = tool_func

    def run(self, prompt: str) -> dict:
        state = {"messages": [prompt], "iterations": 0}

        while state["iterations"] < 5:
            state["iterations"] += 1
            last = state["messages"][-1]

            if "calculate" in last:
                # agent decides to call tool
                res = self.tool_func(last)
                state["messages"].append(f"Tool Result: {res}")
            else:
                # agent finishes
                state["messages"].append("Final Answer: Completed.")
                break

        return state

def test_minimal_graph_agent():
    agent = SimpleStateGraphAgent(lambda text: "Calculated 42")
    final_state = agent.run("Please calculate the metric")

    assert len(final_state["messages"]) == 3
    assert "Tool Result: Calculated 42" in final_state["messages"][1]
    assert "Final Answer: Completed." in final_state["messages"][2]

if __name__ == '__main__':
    test_minimal_graph_agent()
    print("✓ Task 15 passed!")
''')
]

catalog_lines = [
    "# Hour 5 Practical Challenges Catalog",
    "",
    "Tier: **Advanced** | Focus: `Tool Calling with LLMs & LangGraph Core Abstractions`",
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
Curriculum Tier: Advanced | Focus: Tool Calling & LangGraph Basics
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

print("Generated Hour 5 successfully via Python.")
