import os

hour_dir = "practical/hour_1"
os.makedirs(hour_dir, exist_ok=True)

tasks = [
    ("task_01_env_setup.py", "LC-H1-P01", "Environment Configuration & API Key Loader", """
Define a function `load_gemini_credentials(env_dict=None)` that loads and verifies the `GOOGLE_API_KEY`.
It should validate that the key exists, is non-empty, and does not contain whitespace.
""", """
import os

def load_gemini_credentials(env_dict=None):
    if env_dict is not None:
        key = env_dict.get("GOOGLE_API_KEY")
    else:
        key = os.getenv("GOOGLE_API_KEY")
    
    if not key or not isinstance(key, str) or not key.strip():
        raise ValueError("GOOGLE_API_KEY must be a non-empty string.")
    
    clean_key = key.strip()
    return {"GOOGLE_API_KEY": clean_key}

def test_credentials():
    # Valid key
    creds = load_gemini_credentials({"GOOGLE_API_KEY": "AIzaSyFakeKey123"})
    assert creds["GOOGLE_API_KEY"] == "AIzaSyFakeKey123"

    # Missing key raises ValueError
    try:
        load_gemini_credentials({})
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "GOOGLE_API_KEY" in str(e)

    # Empty key raises ValueError
    try:
        load_gemini_credentials({"GOOGLE_API_KEY": "   "})
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "GOOGLE_API_KEY" in str(e)

if __name__ == '__main__':
    test_credentials()
    print("✓ Task 01 passed!")
"""),

    ("task_02_message_types.py", "LC-H1-P02", "LangChain Base Message Types", """
Implement core LangChain message classes: `BaseMessage`, `SystemMessage`, `HumanMessage`, and `AIMessage`.
Each message must store `content` and return its canonical `role` ('system', 'human', or 'ai').
""", """
class BaseMessage:
    def __init__(self, content: str):
        self.content = content

    @property
    def role(self) -> str:
        raise NotImplementedError

class SystemMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "system"

class HumanMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "human"

class AIMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "ai"

def test_message_types():
    sys_msg = SystemMessage("You are an expert tutor.")
    human_msg = HumanMessage("Explain LLMs.")
    ai_msg = AIMessage("LLMs are neural networks...")

    assert sys_msg.role == "system" and sys_msg.content == "You are an expert tutor."
    assert human_msg.role == "human" and human_msg.content == "Explain LLMs."
    assert ai_msg.role == "ai" and "neural networks" in ai_msg.content

if __name__ == '__main__':
    test_message_types()
    print("✓ Task 02 passed!")
"""),

    ("task_03_chat_model_interface.py", "LC-H1-P03", "Chat Model Abstraction & Invocation", """
Implement a `MockChatGoogleGenerativeAI` model that accepts a model name (e.g. 'gemini-1.5-flash')
and temperature. Its `.invoke(messages)` method should accept a list of messages and return an `AIMessage`.
""", """
class BaseMessage:
    def __init__(self, content: str):
        self.content = content

class AIMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "ai"

class MockChatGoogleGenerativeAI:
    def __init__(self, model: str = "gemini-1.5-flash", temperature: float = 0.7):
        self.model = model
        self.temperature = temperature

    def invoke(self, messages):
        if not messages:
            raise ValueError("Messages list cannot be empty.")
        last_message = messages[-1]
        response_content = f"Response from {self.model} to: {last_message.content}"
        return AIMessage(response_content)

def test_model_invoke():
    model = MockChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)
    assert model.model == "gemini-1.5-flash"
    assert model.temperature == 0.2

    msg = BaseMessage("What is LangChain?")
    response = model.invoke([msg])
    assert isinstance(response, AIMessage)
    assert "Response from gemini-1.5-flash to: What is LangChain?" == response.content

if __name__ == '__main__':
    test_model_invoke()
    print("✓ Task 03 passed!")
"""),

    ("task_04_streaming_simulation.py", "LC-H1-P04", "Simulating Model Streaming Chunks", """
Implement a streaming method `.stream(prompt)` on the chat model that yields token chunks
as small string tokens, allowing consumers to process tokens incrementally.
""", """
class MockStreamingChatModel:
    def __init__(self, model_name: str = "gemini-1.5-flash"):
        self.model_name = model_name

    def stream(self, prompt: str):
        words = f"Echo: {prompt}".split()
        for word in words:
            yield word + " "

def test_streaming():
    model = MockStreamingChatModel()
    chunks = list(model.stream("Hello world from LangChain"))
    assert len(chunks) == 5
    accumulated = "".join(chunks).strip()
    assert accumulated == "Echo: Hello world from LangChain"

if __name__ == '__main__':
    test_streaming()
    print("✓ Task 04 passed!")
"""),

    ("task_05_prompt_template_basic.py", "LC-H1-P05", "PromptTemplate Formatting", """
Implement a lightweight `PromptTemplate` class with `.from_template(template_str)` and `.format(**kwargs)`
that automatically detects placeholders like `{topic}` and formats the template string.
""", """
import re

class PromptTemplate:
    def __init__(self, template: str, input_variables: list):
        self.template = template
        self.input_variables = input_variables

    @classmethod
    def from_template(cls, template_str: str):
        variables = re.findall(r'\{([a-zA-Z_0-9]+)\}', template_str)
        return cls(template=template_str, input_variables=variables)

    def format(self, **kwargs) -> str:
        for var in self.input_variables:
            if var not in kwargs:
                raise KeyError(f"Missing required prompt variable: {var}")
        return self.template.format(**kwargs)

def test_prompt_template():
    pt = PromptTemplate.from_template("Write a comprehensive summary of {topic} for {audience}.")
    assert set(pt.input_variables) == {"topic", "audience"}

    formatted = pt.format(topic="Quantum Computing", audience="beginners")
    assert formatted == "Write a comprehensive summary of Quantum Computing for beginners."

    try:
        pt.format(topic="Quantum Computing")
        assert False, "Should raise KeyError for missing audience"
    except KeyError:
        pass

if __name__ == '__main__':
    test_prompt_template()
    print("✓ Task 05 passed!")
"""),

    ("task_06_chat_prompt_template.py", "LC-H1-P06", "ChatPromptTemplate with Roles", """
Create a `ChatPromptTemplate` that accepts a list of tuples `(role, template)` (e.g. `[("system", "..."), ("human", "...")]`)
and formats them into a list of typed messages.
""", """
class BaseMessage:
    def __init__(self, content: str):
        self.content = content

class SystemMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "system"

class HumanMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "human"

class AIMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "ai"

class ChatPromptTemplate:
    def __init__(self, message_templates: list):
        self.message_templates = message_templates

    @classmethod
    def from_messages(cls, templates: list):
        return cls(templates)

    def format_messages(self, **kwargs):
        formatted_messages = []
        for role, template in self.message_templates:
            content = template.format(**kwargs)
            if role == "system":
                formatted_messages.append(SystemMessage(content))
            elif role == "human":
                formatted_messages.append(HumanMessage(content))
            elif role == "ai":
                formatted_messages.append(AIMessage(content))
        return formatted_messages

def test_chat_prompt_template():
    chat_template = ChatPromptTemplate.from_messages([
        ("system", "You are an AI assistant specialized in {domain}."),
        ("human", "Explain {concept} in simple terms.")
    ])

    messages = chat_template.format_messages(domain="Machine Learning", concept="Gradient Descent")
    assert len(messages) == 2
    assert messages[0].role == "system"
    assert "Machine Learning" in messages[0].content
    assert messages[1].role == "human"
    assert "Gradient Descent" in messages[1].content

if __name__ == '__main__':
    test_chat_prompt_template()
    print("✓ Task 06 passed!")
"""),

    ("task_07_structured_output_pydantic.py", "LC-H1-P07", "Structured Output with Pydantic Schema", """
Define a Pydantic model `ReportSummary` with fields `title` (str), `key_points` (list of str),
and `word_count` (int). Implement a parser `parse_report_json(json_str)` that validates and returns the instance.
""", """
from pydantic import BaseModel, Field
import json

class ReportSummary(BaseModel):
    title: str = Field(description="The main title of the generated report")
    key_points: list[str] = Field(description="List of key points")
    word_count: int = Field(ge=0, description="Estimated total word count")

def parse_report_json(json_str: str) -> ReportSummary:
    data = json.loads(json_str)
    return ReportSummary.model_validate(data)

def test_structured_output():
    valid_json = '{"title": "AI in 2026", "key_points": ["LLMs everywhere", "Agent systems"], "word_count": 450}'
    report = parse_report_json(valid_json)
    assert report.title == "AI in 2026"
    assert len(report.key_points) == 2
    assert report.word_count == 450

    invalid_json = '{"title": "Broken", "key_points": "Not a list", "word_count": -5}'
    try:
        parse_report_json(invalid_json)
        assert False, "Should raise ValidationError"
    except Exception:
        pass

if __name__ == '__main__':
    test_structured_output()
    print("✓ Task 07 passed!")
"""),

    ("task_08_structured_output_typeddict.py", "LC-H1-P08", "TypedDict Structured Output Schema", """
Define a `TypedDict` schema `MovieInfo` and a parsing function `validate_movie_dict(data)`
that ensures mandatory keys ('title', 'year', 'genres') and types exist.
""", """
from typing import TypedDict, List

class MovieInfo(TypedDict):
    title: str
    year: int
    genres: List[str]

def validate_movie_dict(data: dict) -> MovieInfo:
    if not isinstance(data.get("title"), str):
        raise TypeError("Title must be a string")
    if not isinstance(data.get("year"), int):
        raise TypeError("Year must be an integer")
    if not isinstance(data.get("genres"), list) or not all(isinstance(g, str) for g in data["genres"]):
        raise TypeError("Genres must be a list of strings")
    return MovieInfo(title=data["title"], year=data["year"], genres=data["genres"])

def test_typeddict_validation():
    data = {"title": "Inception", "year": 2010, "genres": ["Sci-Fi", "Action"]}
    result = validate_movie_dict(data)
    assert result["title"] == "Inception"
    assert result["year"] == 2010
    assert len(result["genres"]) == 2

if __name__ == '__main__':
    test_typeddict_validation()
    print("✓ Task 08 passed!")
"""),

    ("task_09_multi_turn_history.py", "LC-H1-P09", "Multi-Turn Chat History Buffer", """
Implement a `ChatMessageHistory` class that stores conversation turns, allows adding user and AI messages,
and formats them for subsequent model context.
""", """
class BaseMessage:
    def __init__(self, content: str):
        self.content = content

class HumanMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "human"

class AIMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "ai"

class ChatMessageHistory:
    def __init__(self):
        self.messages = []

    def add_user_message(self, message: str):
        self.messages.append(HumanMessage(message))

    def add_ai_message(self, message: str):
        self.messages.append(AIMessage(message))

    def clear(self):
        self.messages.clear()

    def get_transcript(self) -> str:
        lines = []
        for m in self.messages:
            prefix = "User" if m.role == "human" else "AI"
            lines.append(f"{prefix}: {m.content}")
        return "\\n".join(lines)

def test_chat_history():
    history = ChatMessageHistory()
    history.add_user_message("Hello, my name is Alex.")
    history.add_ai_message("Hello Alex! How can I assist you today?")
    history.add_user_message("What is my name?")

    assert len(history.messages) == 3
    transcript = history.get_transcript()
    assert "User: Hello, my name is Alex." in transcript
    assert "AI: Hello Alex!" in transcript

if __name__ == '__main__':
    test_chat_history()
    print("✓ Task 09 passed!")
"""),

    ("task_10_prompt_composition.py", "LC-H1-P10", "Prompt Composition Pipeline", """
Implement a prompt composer that joins a base system instruction with dynamic task instructions
and format constraints into a unified single prompt string.
""", """
def compose_prompt(system_role: str, user_task: str, formatting_constraint: str) -> str:
    parts = [
        f"### System Instructions:\\n{system_role.strip()}",
        f"### User Task:\\n{user_task.strip()}",
        f"### Output Format:\\n{formatting_constraint.strip()}"
    ]
    return "\\n\\n".join(parts)

def test_prompt_composition():
    composed = compose_prompt(
        system_role="You are a senior Python architect.",
        user_task="Refactor this function for O(n) runtime.",
        formatting_constraint="Return valid Python code inside markdown blocks only."
    )
    assert "System Instructions:" in composed
    assert "senior Python architect" in composed
    assert "O(n) runtime" in composed
    assert "Output Format:" in composed

if __name__ == '__main__':
    test_prompt_composition()
    print("✓ Task 10 passed!")
"""),

    ("task_11_temperature_behavior.py", "LC-H1-P11", "Model Configuration & Temperature Validation", """
Implement a `ModelConfig` class that validates temperature bounds (must be between 0.0 and 2.0)
and validates model name against supported Gemini models (`gemini-1.5-flash`, `gemini-1.5-pro`, `gemini-2.0-flash`).
""", """
class ModelConfig:
    SUPPORTED_MODELS = {"gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.0-flash"}

    def __init__(self, model: str, temperature: float = 0.7, max_tokens: int = 1000):
        if model not in self.SUPPORTED_MODELS:
            raise ValueError(f"Model '{model}' is not supported. Choose from {self.SUPPORTED_MODELS}")
        if not (0.0 <= temperature <= 2.0):
            raise ValueError("Temperature must be between 0.0 and 2.0")
        if max_tokens <= 0:
            raise ValueError("max_tokens must be positive")

        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

def test_model_config():
    cfg = ModelConfig("gemini-1.5-flash", temperature=0.5, max_tokens=500)
    assert cfg.model == "gemini-1.5-flash"
    assert cfg.temperature == 0.5

    try:
        ModelConfig("unknown-model")
        assert False, "Should raise ValueError for unsupported model"
    except ValueError:
        pass

    try:
        ModelConfig("gemini-1.5-flash", temperature=2.5)
        assert False, "Should raise ValueError for temperature > 2.0"
    except ValueError:
        pass

if __name__ == '__main__':
    test_model_config()
    print("✓ Task 11 passed!")
"""),

    ("task_12_schema_validation_error.py", "LC-H1-P12", "Catching Schema Validation Errors", """
Implement a safe parser `safe_parse_json(json_str, schema_cls)` that returns a tuple `(instance, error_message)`.
If parsing succeeds, error_message is None; if it fails, instance is None and error_message contains details.
""", """
from pydantic import BaseModel, ValidationError
import json

class SentimentOutput(BaseModel):
    sentiment: str
    confidence: float

def safe_parse_json(json_str: str, schema_cls):
    try:
        data = json.loads(json_str)
        instance = schema_cls.model_validate(data)
        return (instance, None)
    except (json.JSONDecodeError, ValidationError, Exception) as e:
        return (None, str(e))

def test_safe_parse():
    success_json = '{"sentiment": "positive", "confidence": 0.95}'
    inst, err = safe_parse_json(success_json, SentimentOutput)
    assert inst is not None and err is None
    assert inst.sentiment == "positive"
    assert inst.confidence == 0.95

    fail_json = '{"sentiment": "positive", "confidence": "high"}'
    inst, err = safe_parse_json(fail_json, SentimentOutput)
    assert inst is None and err is not None

if __name__ == '__main__':
    test_safe_parse()
    print("✓ Task 12 passed!")
"""),

    ("task_13_message_serialization.py", "LC-H1-P13", "Message List Serialization & Deserialization", """
Implement `serialize_messages(messages)` and `deserialize_messages(dicts)` that convert
between a list of message objects (`SystemMessage`, `HumanMessage`, `AIMessage`) and list of dictionaries.
""", """
class BaseMessage:
    def __init__(self, content: str):
        self.content = content

class SystemMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "system"

class HumanMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "human"

class AIMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "ai"

def serialize_messages(messages: list) -> list:
    return [{"role": m.role, "content": m.content} for m in messages]

def deserialize_messages(dicts: list) -> list:
    mapping = {
        "system": SystemMessage,
        "human": HumanMessage,
        "ai": AIMessage
    }
    result = []
    for d in dicts:
        role = d["role"]
        cls = mapping.get(role)
        if not cls:
            raise ValueError(f"Unknown message role: {role}")
        result.append(cls(d["content"]))
    return result

def test_serialization():
    original = [
        SystemMessage("Be concise."),
        HumanMessage("Hello."),
        AIMessage("Hi there!")
    ]
    serialized = serialize_messages(original)
    assert len(serialized) == 3
    assert serialized[0] == {"role": "system", "content": "Be concise."}

    deserialized = deserialize_messages(serialized)
    assert len(deserialized) == 3
    assert deserialized[1].role == "human"
    assert deserialized[1].content == "Hello."

if __name__ == '__main__':
    test_serialization()
    print("✓ Task 13 passed!")
"""),

    ("task_14_partial_variables.py", "LC-H1-P14", "PromptTemplate Partial Variable Binding", """
Implement partial formatting on `PromptTemplate` where some variables (e.g. `language`) are bound
in advance, returning a new template that only requires the remaining variables (e.g. `code`).
""", """
import re

class PromptTemplate:
    def __init__(self, template: str, input_variables: list):
        self.template = template
        self.input_variables = input_variables

    @classmethod
    def from_template(cls, template_str: str):
        variables = re.findall(r'\{([a-zA-Z_0-9]+)\}', template_str)
        return cls(template=template_str, input_variables=variables)

    def format(self, **kwargs) -> str:
        for var in self.input_variables:
            if var not in kwargs:
                raise KeyError(f"Missing required prompt variable: {var}")
        return self.template.format(**kwargs)

def bind_partial_variable(template: PromptTemplate, **fixed_kwargs) -> PromptTemplate:
    remaining_vars = [v for v in template.input_variables if v not in fixed_kwargs]
    partially_formatted = template.template
    for k, v in fixed_kwargs.items():
        partially_formatted = partially_formatted.replace(f"{{{k}}}", str(v))
    return PromptTemplate(partially_formatted, remaining_vars)

def test_partial_binding():
    base_pt = PromptTemplate.from_template("Translate the following {language} snippet to {target_lang}: {code}")
    assert set(base_pt.input_variables) == {"language", "target_lang", "code"}

    python_pt = bind_partial_variable(base_pt, language="Python", target_lang="Go")
    assert python_pt.input_variables == ["code"]

    res = python_pt.format(code="print('hi')")
    assert res == "Translate the following Python snippet to Go: print('hi')"

if __name__ == '__main__':
    test_partial_binding()
    print("✓ Task 14 passed!")
"""),

    ("task_15_chat_conversation_runner.py", "LC-H1-P15", "Interactive Multi-Turn Dialogue Simulation", """
Implement a conversation simulation runner `simulate_conversation(user_inputs, model)` that:
1. Maintains full conversation history
2. Stops when the user types 'exit' or inputs are exhausted
3. Returns the list of all turns and final message count.
""", """
class BaseMessage:
    def __init__(self, content: str):
        self.content = content

class HumanMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "human"

class AIMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "ai"

class MockChatModel:
    def invoke(self, messages):
        last_msg = messages[-1].content
        return AIMessage(f"Response to: {last_msg}")

def simulate_conversation(user_inputs: list, model) -> list:
    history = []
    for user_text in user_inputs:
        if user_text.strip().lower() == "exit":
            break
        human_msg = HumanMessage(user_text)
        history.append(human_msg)
        response = model.invoke(history)
        history.append(response)
    return history

def test_conversation_runner():
    model = MockChatModel()
    inputs = ["Hello", "What is LangChain?", "exit", "Should not be processed"]
    history = simulate_conversation(inputs, model)

    assert len(history) == 4
    assert history[0].role == "human" and history[0].content == "Hello"
    assert history[1].role == "ai"
    assert history[2].role == "human" and history[2].content == "What is LangChain?"
    assert history[3].role == "ai"

if __name__ == '__main__':
    test_conversation_runner()
    print("✓ Task 15 passed!")
""")
]

catalog_lines = [
    "# Hour 1 Practical Challenges Catalog",
    "",
    "Tier: **Beginner** | Focus: `LangChain Fundamentals, Chat Models & Prompt Engineering`",
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
Curriculum Tier: Beginner | Focus: LangChain Setup & Prompts
Task:
{desc.strip()}

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
{code.strip()}
'''
    with open(filepath, "w") as f:
        f.write(content)
    
    catalog_lines.append(f"| `{task_id}` | {title} | `Beginner` | [{filename}]({filename}) |")

catalog_path = os.path.join(hour_dir, "README.md")
with open(catalog_path, "w") as f:
    f.write("\n".join(catalog_lines) + "\n")

print("Regenerated Hour 1 self-contained.")
