"""
PRACTICAL CHALLENGE: LCEL Graph Representation & Step Tracking (LC-H2-P12)
=====================================================
ID: LC-H2-P12
Curriculum Tier: Intermediate | Focus: LCEL & Chain Composition
Task:
Implement a step tracker that outputs execution graph flow diagram.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class PipelineInspector:
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
