import os

hour_dir = "practical/hour_4"
os.makedirs(hour_dir, exist_ok=True)

tasks = [
    ("task_01_as_retriever.py", "LC-H4-P01", "Vector Store as_retriever Converter",
"""Implement `.as_retriever(search_type='similarity', search_kwargs={'k': 2})` on a VectorStore
that wraps search queries into a `Retriever` object supporting `.invoke(query)`.""",
r'''class MockVectorStore:
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
'''),

    ("task_02_similarity_score_threshold.py", "LC-H4-P02", "Threshold-Based Retrieval",
"""Implement a retriever that filters out documents with similarity score below `score_threshold`.""",
r'''class ThresholdRetriever:
    def __init__(self, documents_with_scores: list, score_threshold: float = 0.7):
        self.data = documents_with_scores
        self.score_threshold = score_threshold

    def invoke(self, query: str) -> list:
        # returns docs that meet threshold
        return [doc for doc, score in self.data if score >= self.score_threshold]

def test_threshold_retriever():
    data = [
        ("Doc 1: Exact Match", 0.95),
        ("Doc 2: Moderate Match", 0.72),
        ("Doc 3: Low Match", 0.45)
    ]
    retriever = ThresholdRetriever(data, score_threshold=0.7)
    passed_docs = retriever.invoke("Match")

    assert len(passed_docs) == 2
    assert "Doc 1: Exact Match" in passed_docs
    assert "Doc 2: Moderate Match" in passed_docs
    assert "Doc 3: Low Match" not in passed_docs

if __name__ == '__main__':
    test_threshold_retriever()
    print("✓ Task 02 passed!")
'''),

    ("task_03_mmr_retriever.py", "LC-H4-P03", "Maximal Marginal Relevance (MMR) Retrieval",
"""Implement an MMR ranking function that balances query relevance and diversity among selected documents.""",
r'''def mmr_rerank(query_score_map: dict, similarity_matrix: dict, lambda_mult: float = 0.5, k: int = 2) -> list:
    selected = []
    candidates = list(query_score_map.keys())

    while len(selected) < k and candidates:
        best_doc = None
        best_mmr_score = -float('inf')

        for c in candidates:
            sim_to_query = query_score_map[c]
            max_sim_to_selected = max([similarity_matrix.get((c, s), similarity_matrix.get((s, c), 0.0)) for s in selected], default=0.0)
            mmr = lambda_mult * sim_to_query - (1 - lambda_mult) * max_sim_to_selected
            if mmr > best_mmr_score:
                best_mmr_score = mmr
                best_doc = c

        if best_doc is not None:
            selected.append(best_doc)
            candidates.remove(best_doc)

    return selected

def test_mmr():
    query_scores = {"docA": 0.9, "docB": 0.88, "docC": 0.7}
    # docA and docB are near duplicates (sim 0.95), docC is diverse (sim 0.1)
    sim_matrix = {("docA", "docB"): 0.95, ("docA", "docC"): 0.1, ("docB", "docC"): 0.1}

    # High diversity (lambda = 0.2) should pick docA and docC rather than docB
    top_diverse = mmr_rerank(query_scores, sim_matrix, lambda_mult=0.2, k=2)
    assert top_diverse[0] == "docA"
    assert top_diverse[1] == "docC"

if __name__ == '__main__':
    test_mmr()
    print("✓ Task 03 passed!")
'''),

    ("task_04_format_docs.py", "LC-H4-P04", "Formatting Documents for Context Injection",
"""Implement `format_docs(docs)` that concatenates a list of document objects into a clean,
numbered or separated context string with source references.""",
r'''class MockDoc:
    def __init__(self, content: str, source: str):
        self.page_content = content
        self.metadata = {"source": source}

def format_docs(docs: list) -> str:
    parts = []
    for idx, doc in enumerate(docs, start=1):
        source = doc.metadata.get("source", "Unknown")
        parts.append(f"[{idx}] (Source: {source})\n{doc.page_content.strip()}")
    return "\n\n".join(parts)

def test_format_docs():
    docs = [
        MockDoc("LangChain simplifies prompt management.", "chap1.pdf"),
        MockDoc("Vector stores index embeddings efficiently.", "chap2.pdf")
    ]
    formatted = format_docs(docs)
    assert "[1] (Source: chap1.pdf)" in formatted
    assert "[2] (Source: chap2.pdf)" in formatted
    assert "Vector stores index embeddings efficiently." in formatted

if __name__ == '__main__':
    test_format_docs()
    print("✓ Task 04 passed!")
'''),

    ("task_05_grounded_rag_prompt.py", "LC-H4-P05", "Grounded RAG Prompt Builder",
"""Build a prompt generator that explicitly instructs the LLM:
'Answer the question based ONLY on the context below. If you cannot find the answer, reply \"I do not know\".'""",
r'''def create_rag_prompt(context: str, question: str) -> str:
    template = (
        "You are an assistant for question-answering tasks. Use the following pieces of "
        "retrieved context to answer the question. If you do not know the answer based on "
        "the provided context, reply exactly with 'I do not know'. Do not hallucinate.\n\n"
        f"Context:\n{context}\n\n"
        f"Question:\n{question}\n\n"
        "Answer:"
    )
    return template

def test_rag_prompt():
    prompt = create_rag_prompt("RAG stands for Retrieval-Augmented Generation.", "What does RAG mean?")
    assert "retrieved context" in prompt
    assert "'I do not know'" in prompt
    assert "What does RAG mean?" in prompt

if __name__ == '__main__':
    test_rag_prompt()
    print("✓ Task 05 passed!")
'''),

    ("task_06_citation_generator.py", "LC-H4-P06", "Injecting Citations into Answers",
"""Implement `append_citations(answer, sources)` which formats a list of unique source identifiers
and appends a '### Sources:' section at the bottom of the answer.""",
r'''def append_citations(answer: str, sources: list) -> str:
    unique_sources = sorted(list(set(sources)))
    if not unique_sources:
        return answer.strip()
    sources_block = "\n\n### Sources:\n" + "\n".join(f"- {s}" for s in unique_sources)
    return answer.strip() + sources_block

def test_citations():
    raw_answer = "LangGraph enables stateful multi-agent workflows."
    with_sources = append_citations(raw_answer, ["intro.md", "guide.pdf", "intro.md"])

    assert "### Sources:" in with_sources
    assert "- guide.pdf" in with_sources
    assert "- intro.md" in with_sources
    # Verify deduplication (intro.md appears once)
    assert with_sources.count("intro.md") == 1

if __name__ == '__main__':
    test_citations()
    print("✓ Task 06 passed!")
'''),

    ("task_07_rag_pipeline_execution.py", "LC-H4-P07", "End-to-End RAG Execution Simulator",
"""Implement a complete RAG chain runner:
1. Retriever fetches relevant documents for query
2. Context is formatted
3. Grounded prompt is generated
4. LLM produces answer.""",
r'''from task_04_format_docs import MockDoc, format_docs
from task_05_grounded_rag_prompt import create_rag_prompt

class MockRAGSystem:
    def __init__(self, doc_db: list):
        self.doc_db = doc_db

    def retrieve(self, query: str) -> list:
        # substring matching
        matches = [d for d in self.doc_db if any(w.lower() in d.page_content.lower() for w in query.split())]
        return matches

    def generate(self, prompt: str) -> str:
        if "Google Gemini" in prompt:
            return "Gemini is Google's multimodal AI model."
        return "I do not know"

    def ask(self, query: str) -> str:
        docs = self.retrieve(query)
        context = format_docs(docs) if docs else "No relevant context found."
        prompt = create_rag_prompt(context, query)
        return self.generate(prompt)

def test_rag_pipeline():
    docs = [
        MockDoc("Google Gemini models provide strong reasoning and multimodal understanding.", "gemini_spec.txt")
    ]
    rag = MockRAGSystem(docs)

    ans1 = rag.ask("Tell me about Google Gemini")
    assert "Gemini is Google's multimodal AI model." in ans1

    ans2 = rag.ask("What is quantum teleportation?")
    assert ans2 == "I do not know"

if __name__ == '__main__':
    test_rag_pipeline()
    print("✓ Task 07 passed!")
'''),

    ("task_08_tool_decorator.py", "LC-H4-P08", "Custom @tool Decorator",
"""Implement a `@tool` decorator that wraps a Python function, extracts its name, docstring,
and parameter schema, and provides an `.invoke(kwargs)` method.""",
r'''import inspect

class Tool:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
        self.description = (func.__doc__ or "").strip()
        self.signature = inspect.signature(func)

    def invoke(self, kwargs: dict):
        return self.func(**kwargs)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

def tool(func):
    return Tool(func)

@tool
def add(a: int, b: int) -> int:
    """Add two integer numbers together."""
    return a + b

def test_tool_decorator():
    assert add.name == "add"
    assert add.description == "Add two integer numbers together."
    assert add.invoke({"a": 3, "b": 7}) == 10
    assert add(4, 5) == 9

if __name__ == '__main__':
    test_tool_decorator()
    print("✓ Task 08 passed!")
'''),

    ("task_09_tool_schema_extraction.py", "LC-H4-P09", "Tool Parameter Schema Inspection",
"""Implement a schema generator `extract_tool_schema(tool)` that produces a JSON-compatible
schema containing parameter names, types, and default values from type hints.""",
r'''import inspect

def extract_tool_schema(func) -> dict:
    sig = inspect.signature(func)
    params = {}
    for name, p in sig.parameters.items():
        type_name = p.annotation.__name__ if p.annotation != inspect.Parameter.empty else "any"
        has_default = p.default != inspect.Parameter.empty
        params[name] = {
            "type": type_name,
            "required": not has_default,
            "default": p.default if has_default else None
        }
    return {
        "name": func.__name__,
        "description": (func.__doc__ or "").strip(),
        "parameters": params
    }

def multiply(x: int, y: int = 1) -> int:
    """Multiply two integers."""
    return x * y

def test_schema_extraction():
    schema = extract_tool_schema(multiply)
    assert schema["name"] == "multiply"
    assert schema["description"] == "Multiply two integers."
    assert schema["parameters"]["x"]["type"] == "int"
    assert schema["parameters"]["x"]["required"] is True
    assert schema["parameters"]["y"]["default"] == 1

if __name__ == '__main__':
    test_schema_extraction()
    print("✓ Task 09 passed!")
'''),

    ("task_10_multi_argument_tools.py", "LC-H4-P10", "Multi-Argument Mathematical Tools",
"""Implement a set of tools (`calculate_tax(subtotal, rate=0.1)` and `format_currency(amount, currency='USD')`)
and test direct invocations with dictionary inputs.""",
r'''def calculate_tax(subtotal: float, rate: float = 0.1) -> float:
    """Calculates tax amount on a subtotal."""
    return round(subtotal * rate, 2)

def format_currency(amount: float, currency: str = "USD") -> str:
    """Formats numeric amount with currency code."""
    return f"{currency} {amount:.2f}"

def test_multi_arg_tools():
    tax = calculate_tax(subtotal=150.0, rate=0.08)
    assert tax == 12.0
    formatted = format_currency(amount=162.0, currency="USD")
    assert formatted == "USD 162.00"

if __name__ == '__main__':
    test_multi_arg_tools()
    print("✓ Task 10 passed!")
'''),

    ("task_11_tool_docstring_validation.py", "LC-H4-P11", "Enforcing Tool Docstring Standards",
"""Implement a validator `validate_tool_definition(func)` that checks if a tool has a non-empty
docstring, valid type annotations on all parameters, and a return type annotation.""",
r'''import inspect

def validate_tool_definition(func):
    doc = func.__doc__
    if not doc or not doc.strip():
        raise ValueError(f"Tool '{func.__name__}' must contain a descriptive docstring.")
    
    sig = inspect.signature(func)
    for name, p in sig.parameters.items():
        if p.annotation == inspect.Parameter.empty:
            raise TypeError(f"Parameter '{name}' in tool '{func.__name__}' lacks type annotation.")
            
    if sig.return_annotation == inspect.Parameter.empty:
        raise TypeError(f"Tool '{func.__name__}' must have a return type annotation.")
    return True

def valid_tool(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b

def invalid_tool(a, b):
    return a + b

def test_tool_docstring_validation():
    assert validate_tool_definition(valid_tool) is True

    try:
        validate_tool_definition(invalid_tool)
        assert False, "Should fail on missing docstring/types"
    except (ValueError, TypeError):
        pass

if __name__ == '__main__':
    test_tool_docstring_validation()
    print("✓ Task 11 passed!")
'''),

    ("task_12_tool_registry.py", "LC-H4-P12", "Centralized Tool Registry",
"""Implement a `ToolRegistry` that registers tools, prevents duplicate names,
lists registered tools, and allows lookup by tool name.""",
r'''class ToolRegistry:
    def __init__(self):
        self._tools = {}

    def register(self, tool_func):
        name = getattr(tool_func, "name", tool_func.__name__)
        if name in self._tools:
            raise ValueError(f"Tool '{name}' is already registered.")
        self._tools[name] = tool_func

    def get(self, name: str):
        if name not in self._tools:
            raise KeyError(f"Tool '{name}' not found.")
        return self._tools[name]

    def list_names(self) -> list:
        return sorted(list(self._tools.keys()))

def test_tool_registry():
    registry = ToolRegistry()
    def search_web(query: str) -> str: """Search web"""; return ""
    def calculator(expr: str) -> str: """Calc"""; return ""

    registry.register(search_web)
    registry.register(calculator)

    assert registry.list_names() == ["calculator", "search_web"]
    assert registry.get("calculator") == calculator

    try:
        registry.register(search_web)
        assert False, "Duplicate registration should raise ValueError"
    except ValueError:
        pass

if __name__ == '__main__':
    test_tool_registry()
    print("✓ Task 12 passed!")
'''),

    ("task_13_safe_tool_execution.py", "LC-H4-P13", "Safe Tool Execution & Error Recovery",
"""Implement `safe_execute_tool(tool_func, kwargs)` that executes a tool, catches exceptions,
and returns an informative error string instead of crashing the pipeline.""",
r'''def safe_execute_tool(tool_func, kwargs: dict) -> str:
    try:
        result = tool_func(**kwargs)
        return str(result)
    except Exception as e:
        return f"Error executing {tool_func.__name__}: {type(e).__name__} - {str(e)}"

def divide(a: float, b: float) -> float:
    return a / b

def test_safe_tool_execution():
    res1 = safe_execute_tool(divide, {"a": 10.0, "b": 2.0})
    assert res1 == "5.0"

    res2 = safe_execute_tool(divide, {"a": 10.0, "b": 0.0})
    assert "ZeroDivisionError" in res2

if __name__ == '__main__':
    test_safe_tool_execution()
    print("✓ Task 13 passed!")
'''),

    ("task_14_mock_retriever_tool.py", "LC-H4-P14", "Wrapping a Retriever as a Tool",
"""Implement `create_retriever_tool(retriever, name, description)` that returns a callable Tool
accepting `{'query': str}` and returning concatenated retrieved documents.""",
r'''class MockRetriever:
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
'''),

    ("task_15_rag_evaluation_harness.py", "LC-H4-P15", "RAG Output Accuracy & Grounding Evaluator",
"""Implement an evaluation harness `evaluate_grounding(answer, context)` that verifies
whether answer key terms are grounded in the retrieved context.""",
r'''def evaluate_grounding(answer: str, context: str) -> dict:
    ans_words = set(w.lower() for w in answer.split() if len(w) > 4)
    ctx_words = set(w.lower() for w in context.split() if len(w) > 4)

    grounded_words = ans_words.intersection(ctx_words)
    ratio = len(grounded_words) / len(ans_words) if ans_words else 1.0

    return {
        "is_grounded": ratio >= 0.5,
        "grounding_ratio": round(ratio, 2),
        "grounded_terms": sorted(list(grounded_words))
    }

def test_grounding_evaluator():
    ctx = "The LangChain framework enables modular chain construction."
    ans_good = "LangChain enables modular construction."
    ans_hallucination = "Quantum computing relies on superconductors and qubits."

    res_good = evaluate_grounding(ans_good, ctx)
    assert res_good["is_grounded"] is True
    assert "langchain" in res_good["grounded_terms"]

    res_bad = evaluate_grounding(ans_hallucination, ctx)
    assert res_bad["is_grounded"] is False

if __name__ == '__main__':
    test_grounding_evaluator()
    print("✓ Task 15 passed!")
''')
]

catalog_lines = [
    "# Hour 4 Practical Challenges Catalog",
    "",
    "Tier: **Advanced** | Focus: `Retrievers, Grounded RAG Chains & Tool Engineering`",
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
Curriculum Tier: Advanced | Focus: Advanced RAG & Tool Interfaces
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

print("Generated Hour 4 successfully via Python.")
