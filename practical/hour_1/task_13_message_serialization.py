"""
PRACTICAL CHALLENGE: Message List Serialization & Deserialization (LC-H1-P13)
=====================================================
ID: LC-H1-P13
Curriculum Tier: Beginner | Focus: LangChain Setup & Prompts
Task:
Implement `serialize_messages(messages)` and `deserialize_messages(dicts)` that convert
between a list of message objects (`SystemMessage`, `HumanMessage`, `AIMessage`) and list of dictionaries.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
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
