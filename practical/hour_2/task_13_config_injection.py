"""
PRACTICAL CHALLENGE: Runtime Configuration Passing (RunnableConfig) (LC-H2-P13)
=====================================================
ID: LC-H2-P13
Curriculum Tier: Intermediate | Focus: LCEL & Chain Composition
Task:
Implement runtime configuration passing (tags, metadata) through runnable invocations.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class ConfigurableTask:
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
