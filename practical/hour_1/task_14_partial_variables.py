"""
PRACTICAL CHALLENGE: PromptTemplate Partial Variable Binding (LC-H1-P14)
=====================================================
ID: LC-H1-P14
Curriculum Tier: Beginner | Focus: LangChain Setup & Prompts
Task:
Implement partial formatting on `PromptTemplate` where some variables (e.g. `language`) are bound
in advance, returning a new template that only requires the remaining variables (e.g. `code`).

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
