"""
PRACTICAL CHALLENGE: PromptTemplate Formatting (LC-H1-P05)
=====================================================
ID: LC-H1-P05
Curriculum Tier: Beginner | Focus: LangChain Setup & Prompts
Task:
Implement a lightweight `PromptTemplate` class with `.from_template(template_str)` and `.format(**kwargs)`
that automatically detects placeholders like `{topic}` and formats the template string.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
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
