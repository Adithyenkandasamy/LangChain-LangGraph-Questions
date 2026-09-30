"""
PRACTICAL CHALLENGE: ChatPromptTemplate with Roles (LC-H1-P06)
=====================================================
ID: LC-H1-P06
Curriculum Tier: Beginner | Focus: LangChain Setup & Prompts
Task:
Create a `ChatPromptTemplate` that accepts a list of tuples `(role, template)` (e.g. `[("system", "..."), ("human", "...")]`)
and formats them into a list of typed messages.

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
