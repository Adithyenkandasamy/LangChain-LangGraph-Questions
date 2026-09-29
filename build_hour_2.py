import os

hour_dir = "practical/hour_2"
os.makedirs(hour_dir, exist_ok=True)

tasks = [
    ("task_01_pipe_operator.py", "LC-H2-P01", "Runnable Pipe Operator Abstraction",
"""Define a `Runnable` base class supporting the `|` pipe operator to form sequential runnable pipelines.""",
r'''class Runnable:
    def __or__(self, other):
        return RunnableSequence(self, other)

    def invoke(self, input_val):
        raise NotImplementedError

class RunnableSequence(Runnable):
    def __init__(self, first: Runnable, second: Runnable):
        self.first = first
        self.second = second

    def invoke(self, input_val):
        intermediate = self.first.invoke(input_val)
        return self.second.invoke(intermediate)

class AddSuffix(Runnable):
    def __init__(self, suffix: str):
        self.suffix = suffix
    def invoke(self, input_val: str):
        return input_val + self.suffix

def test_pipe_operator():
    step1 = AddSuffix(" -> Step 1")
    step2 = AddSuffix(" -> Step 2")
    chain = step1 | step2
    result = chain.invoke("Start")
    assert result == "Start -> Step 1 -> Step 2"

if __name__ == '__main__':
    test_pipe_operator()
    print("✓ Task 01 passed!")
'''),

    ("task_02_str_output_parser.py", "LC-H2-P02", "StrOutputParser Implementation",
"""Implement StrOutputParser as a Runnable that extracts cleaned text from an AIMessage or dictionary.""",
r'''class AIMessage:
    def __init__(self, content: str):
        self.content = content

class StrOutputParser:
    def invoke(self, input_val) -> str:
        if hasattr(input_val, "content"):
            return str(input_val.content).strip()
        elif isinstance(input_val, dict) and "content" in input_val:
            return str(input_val["content"]).strip()
        return str(input_val).strip()

def test_str_output_parser():
    parser = StrOutputParser()
    msg = AIMessage("  LangChain Expression Language (LCEL)  \n")
    assert parser.invoke(msg) == "LangChain Expression Language (LCEL)"
    assert parser.invoke({"content": "Hello World"}) == "Hello World"
    assert parser.invoke("Raw text") == "Raw text"

if __name__ == '__main__':
    test_str_output_parser()
    print("✓ Task 02 passed!")
'''),

    ("task_03_simple_lcel_chain.py", "LC-H2-P03", "Basic LCEL Prompt and Model Chain",
"""Build a basic LCEL chain combining prompt, model, and parser.""",
r'''class MockPrompt:
    def __init__(self, template: str):
        self.template = template
    def invoke(self, kwargs: dict) -> str:
        return self.template.format(**kwargs)

class MockModel:
    def invoke(self, text: str):
        class Msg:
            def __init__(self, content): self.content = content
        return Msg(f"Detailed answer about: {text}")

class StrOutputParser:
    def invoke(self, msg) -> str:
        return msg.content

class SimpleChain:
    def __init__(self, prompt, model, parser):
        self.prompt = prompt
        self.model = model
        self.parser = parser

    def invoke(self, inputs: dict) -> str:
        p_out = self.prompt.invoke(inputs)
        m_out = self.model.invoke(p_out)
        return self.parser.invoke(m_out)

def test_simple_chain():
    prompt = MockPrompt("Explain {topic} in one sentence.")
    model = MockModel()
    parser = StrOutputParser()
    chain = SimpleChain(prompt, model, parser)

    out = chain.invoke({"topic": "Vector Stores"})
    assert out == "Detailed answer about: Explain Vector Stores in one sentence."

if __name__ == '__main__':
    test_simple_chain()
    print("✓ Task 03 passed!")
'''),

    ("task_04_sequential_chain.py", "LC-H2-P04", "Two-Stage Sequential Chain",
"""Implement a two-stage sequential chain where stage 1 output feeds into stage 2 input.""",
r'''class OutlineGenerator:
    def invoke(self, inputs: dict) -> dict:
        topic = inputs["topic"]
        return {"outline": f"1. Intro to {topic}\n2. Core Mechanisms\n3. Future Trends"}

class SummaryGenerator:
    def invoke(self, inputs: dict) -> str:
        outline = inputs["outline"]
        return f"Summary of points:\n- {outline.replace(chr(10), ' | ')}"

class SequentialChain:
    def __init__(self, stage1, stage2):
        self.stage1 = stage1
        self.stage2 = stage2

    def invoke(self, inputs: dict) -> str:
        s1_out = self.stage1.invoke(inputs)
        return self.stage2.invoke(s1_out)

def test_sequential_chain():
    chain = SequentialChain(OutlineGenerator(), SummaryGenerator())
    res = chain.invoke({"topic": "LangGraph"})
    assert "Summary of points:" in res
    assert "1. Intro to LangGraph" in res
    assert "3. Future Trends" in res

if __name__ == '__main__':
    test_sequential_chain()
    print("✓ Task 04 passed!")
'''),

    ("task_05_runnable_passthrough.py", "LC-H2-P05", "RunnablePassthrough Identity Function",
"""Implement RunnablePassthrough and RunnablePassthrough.assign for context passing.""",
r'''class RunnablePassthrough:
    def invoke(self, x):
        return x

    @classmethod
    def assign(cls, **extra_fns):
        return RunnableAssign(extra_fns)

class RunnableAssign:
    def __init__(self, fns: dict):
        self.fns = fns

    def invoke(self, input_dict: dict) -> dict:
        result = dict(input_dict)
        for key, fn in self.fns.items():
            result[key] = fn(result)
        return result

def test_runnable_passthrough():
    passthrough = RunnablePassthrough()
    assert passthrough.invoke({"query": "AI"}) == {"query": "AI"}

    assigner = RunnablePassthrough.assign(
        word_count=lambda d: len(d["text"].split()),
        upper_text=lambda d: d["text"].upper()
    )
    res = assigner.invoke({"text": "hello langchain developers"})
    assert res["word_count"] == 3
    assert res["upper_text"] == "HELLO LANGCHAIN DEVELOPERS"
    assert res["text"] == "hello langchain developers"

if __name__ == '__main__':
    test_runnable_passthrough()
    print("✓ Task 05 passed!")
'''),

    ("task_06_runnable_parallel.py", "LC-H2-P06", "RunnableParallel Concurrent Mapping",
"""Implement RunnableParallel for concurrent branch execution.""",
r'''class RunnableParallel:
    def __init__(self, branches: dict):
        self.branches = branches

    def invoke(self, input_val) -> dict:
        results = {}
        for key, runnable in self.branches.items():
            results[key] = runnable(input_val) if callable(runnable) else runnable.invoke(input_val)
        return results

def test_runnable_parallel():
    parallel = RunnableParallel({
        "length": lambda text: len(text),
        "words": lambda text: len(text.split()),
        "first_word": lambda text: text.split()[0] if text.split() else ""
    })

    out = parallel.invoke("LangChain simplifies AI engineering")
    assert out["length"] == len("LangChain simplifies AI engineering")
    assert out["words"] == 4
    assert out["first_word"] == "LangChain"

if __name__ == '__main__':
    test_runnable_parallel()
    print("✓ Task 06 passed!")
'''),

    ("task_07_combining_parallel_branches.py", "LC-H2-P07", "Synthesizing Parallel Outputs",
"""Implement an analysis pipeline synthesizing outputs from parallel branches into a unified summary.""",
r'''def extract_sentiment(review: str) -> str:
    low = review.lower()
    if "good" in low or "great" in low or "love" in low:
        return "Positive"
    return "Negative"

def extract_topics(review: str) -> list:
    topics = []
    if "battery" in review.lower(): topics.append("battery")
    if "screen" in review.lower(): topics.append("screen")
    if "camera" in review.lower(): topics.append("camera")
    return topics

def synthesize_report(data: dict) -> str:
    return f"Review Sentiment: {data['sentiment']} | Mentioned Features: {', '.join(data['topics'])}"

def analyze_review(review_text: str) -> str:
    parallel_outputs = {
        "sentiment": extract_sentiment(review_text),
        "topics": extract_topics(review_text)
    }
    return synthesize_report(parallel_outputs)

def test_combining_parallel():
    review = "I love the screen resolution and battery life on this phone!"
    report = analyze_review(review)
    assert "Review Sentiment: Positive" in report
    assert "battery" in report and "screen" in report

if __name__ == '__main__':
    test_combining_parallel()
    print("✓ Task 07 passed!")
'''),

    ("task_08_runnable_lambda.py", "LC-H2-P08", "RunnableLambda Custom Transformations",
"""Implement RunnableLambda to convert any Python callable into a pipeable Runnable.""",
r'''class RunnableLambda:
    def __init__(self, func):
        self.func = func

    def invoke(self, input_val):
        return self.func(input_val)

    def __or__(self, other):
        return RunnableLambda(lambda x: other.invoke(self.invoke(x)))

def test_runnable_lambda():
    double_fn = RunnableLambda(lambda x: x * 2)
    add_five = RunnableLambda(lambda x: x + 5)
    to_string = RunnableLambda(lambda x: f"Result: {x}")

    chain = double_fn | add_five | to_string
    assert chain.invoke(10) == "Result: 25"

if __name__ == '__main__':
    test_runnable_lambda()
    print("✓ Task 08 passed!")
'''),

    ("task_09_runnable_fallbacks.py", "LC-H2-P09", "Resilient Chains with Fallbacks",
"""Implement a fallback runner that recovers gracefully when primary step encounters exceptions.""",
r'''class FallbackRunner:
    def __init__(self, primary, fallbacks: list):
        self.primary = primary
        self.fallbacks = fallbacks

    def invoke(self, input_val):
        try:
            return self.primary(input_val)
        except Exception:
            for fb in self.fallbacks:
                try:
                    return fb(input_val)
                except Exception:
                    continue
            raise RuntimeError("All fallbacks failed.")

def test_fallbacks():
    failing_primary = lambda x: 1 / 0
    secondary_fail = lambda x: [][5]
    successful_fallback = lambda x: f"Recovered with: {x}"

    runner = FallbackRunner(failing_primary, [secondary_fail, successful_fallback])
    res = runner.invoke("TestInput")
    assert res == "Recovered with: TestInput"

if __name__ == '__main__':
    test_fallbacks()
    print("✓ Task 09 passed!")
'''),

    ("task_10_conditional_branching.py", "LC-H2-P10", "Dynamic Branch Routing (RunnableBranch)",
"""Implement RunnableBranch to direct input dynamically to matching logic handler.""",
r'''class RunnableBranch:
    def __init__(self, branches: list, default_branch):
        self.branches = branches
        self.default_branch = default_branch

    def invoke(self, input_val):
        for condition_fn, runnable in self.branches:
            if condition_fn(input_val):
                return runnable(input_val)
        return self.default_branch(input_val)

def test_conditional_branch():
    branch = RunnableBranch(
        branches=[
            (lambda x: x["category"] == "math", lambda x: f"Math: {eval(x['query'])}"),
            (lambda x: x["category"] == "greet", lambda x: f"Greeting: Hello {x['name']}!")
        ],
        default_branch=lambda x: f"General query: {x.get('query', '')}"
    )

    assert branch.invoke({"category": "math", "query": "2 + 3"}) == "Math: 5"
    assert branch.invoke({"category": "greet", "name": "Alice"}) == "Greeting: Hello Alice!"
    assert branch.invoke({"category": "other", "query": "weather today"}) == "General query: weather today"

if __name__ == '__main__':
    test_conditional_branch()
    print("✓ Task 10 passed!")
'''),

    ("task_11_batch_processing.py", "LC-H2-P11", "Batch Invocation Support",
"""Implement batch execution on runnables maintaining item ordering.""",
r'''class BatchableRunnable:
    def __init__(self, transform_fn):
        self.transform_fn = transform_fn

    def invoke(self, item):
        return self.transform_fn(item)

    def batch(self, items: list) -> list:
        return [self.invoke(item) for item in items]

def test_batch():
    runnable = BatchableRunnable(lambda text: f"Processed: {text.title()}")
    inputs = ["langchain", "prompt template", "vector database"]
    outputs = runnable.batch(inputs)

    assert outputs == [
        "Processed: Langchain",
        "Processed: Prompt Template",
        "Processed: Vector Database"
    ]

if __name__ == '__main__':
    test_batch()
    print("✓ Task 11 passed!")
'''),

    ("task_12_graph_inspection.py", "LC-H2-P12", "LCEL Graph Representation & Step Tracking",
"""Implement a step tracker that outputs execution graph flow diagram.""",
r'''class PipelineInspector:
    def __init__(self):
        self.steps = []

    def add_step(self, step_name: str):
        self.steps.append(step_name)

    def get_flow_diagram(self) -> str:
        return " -> ".join(self.steps)

def test_graph_inspection():
    inspector = PipelineInspector()
    inspector.add_step("PromptTemplate")
    inspector.add_step("ChatGoogleGenerativeAI")
    inspector.add_step("StrOutputParser")

    assert len(inspector.steps) == 3
    assert inspector.get_flow_diagram() == "PromptTemplate -> ChatGoogleGenerativeAI -> StrOutputParser"

if __name__ == '__main__':
    test_graph_inspection()
    print("✓ Task 12 passed!")
'''),

    ("task_13_config_injection.py", "LC-H2-P13", "Runtime Configuration Passing (RunnableConfig)",
"""Implement runtime configuration passing (tags, metadata) through runnable invocations.""",
r'''class ConfigurableTask:
    def invoke(self, input_val: str, config: dict = None) -> dict:
        config = config or {}
        tags = config.get("tags", [])
        return {
            "result": f"Output for {input_val}",
            "executed_with_tags": tags,
            "has_debug": "debug" in tags
        }

def test_config_injection():
    task = ConfigurableTask()
    res1 = task.invoke("Test 1")
    assert res1["executed_with_tags"] == []
    assert not res1["has_debug"]

    res2 = task.invoke("Test 2", config={"tags": ["debug", "v1"]})
    assert res2["executed_with_tags"] == ["debug", "v1"]
    assert res2["has_debug"] is True

if __name__ == '__main__':
    test_config_injection()
    print("✓ Task 13 passed!")
'''),

    ("task_14_input_validation_chain.py", "LC-H2-P14", "Validating Inputs in LCEL Pipeline",
"""Implement pre-execution input validator ensuring required dictionary keys are provided.""",
r'''class InputValidator:
    def __init__(self, required_keys: set):
        self.required_keys = required_keys

    def invoke(self, inputs: dict) -> dict:
        missing = self.required_keys - set(inputs.keys())
        if missing:
            raise ValueError(f"Missing required input keys: {sorted(list(missing))}")
        return inputs

def test_input_validation_chain():
    validator = InputValidator(required_keys={"topic", "language"})
    valid_input = {"topic": "Async IO", "language": "Python", "extra": 123}
    assert validator.invoke(valid_input) == valid_input

    try:
        validator.invoke({"topic": "Async IO"})
        assert False, "Should fail on missing 'language'"
    except ValueError as e:
        assert "language" in str(e)

if __name__ == '__main__':
    test_input_validation_chain()
    print("✓ Task 14 passed!")
'''),

    ("task_15_end_to_end_sequential_pipeline.py", "LC-H2-P15", "Complete End-to-End Multi-Step Pipeline",
"""Build a complete multi-stage text processing pipeline with cleaning, validation, and summarization.""",
r'''class ArticlePipeline:
    def __init__(self):
        pass

    def run(self, inputs: dict) -> dict:
        if "raw_text" not in inputs:
            raise KeyError("Input must contain 'raw_text'")
        cleaned = " ".join(inputs["raw_text"].strip().split())
        summary = f"Summary: {cleaned[:40]}..."
        return {
            "original_length": len(inputs["raw_text"]),
            "cleaned_text": cleaned,
            "summary": summary,
            "status": "PROCESSED"
        }

def test_end_to_end_pipeline():
    pipeline = ArticlePipeline()
    payload = {"raw_text": "   LangChain   Expression    Language enables easy composition of chains.   "}
    result = pipeline.run(payload)

    assert result["status"] == "PROCESSED"
    assert result["cleaned_text"] == "LangChain Expression Language enables easy composition of chains."
    assert "Summary: LangChain Expression Language enables ea..." == result["summary"]

if __name__ == '__main__':
    test_end_to_end_pipeline()
    print("✓ Task 15 passed!")
''')
]

catalog_lines = [
    "# Hour 2 Practical Challenges Catalog",
    "",
    "Tier: **Intermediate** | Focus: `LCEL, Sequential & Parallel Chains, and Branching`",
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
Curriculum Tier: Intermediate | Focus: LCEL & Chain Composition
Task:
{desc.strip()}

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
{code.strip()}
'''
    with open(filepath, "w") as f:
        f.write(content)
    
    catalog_lines.append(f"| `{task_id}` | {title} | `Intermediate` | [{filename}]({filename}) |")

catalog_path = os.path.join(hour_dir, "README.md")
with open(catalog_path, "w") as f:
    f.write("\n".join(catalog_lines) + "\n")

print("Generated Hour 2 successfully via Python.")
