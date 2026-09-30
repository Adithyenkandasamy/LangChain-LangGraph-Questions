"""
PRACTICAL CHALLENGE: Multi-Turn Conversation Memory Window (LC-H7-P09)
=====================================================
ID: LC-H7-P09
Curriculum Tier: Mastery | Focus: Autonomous LangGraph RAG Agent
Task:
Implement a `ConversationWindowMemory(k=4)` that retains only the last `k` messages
to prevent token overflow while maintaining the initial system prompt.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class ConversationWindowMemory:
    def __init__(self, k: int = 4):
        self.k = k

    def trim(self, messages: list) -> list:
        if len(messages) <= self.k:
            return list(messages)
        system_msgs = [m for m in messages if m.get("role") == "system"]
        non_system = [m for m in messages if m.get("role") != "system"]
        trimmed_non_system = non_system[-self.k:]
        return system_msgs + trimmed_non_system

def test_memory_trim():
    mem = ConversationWindowMemory(k=3)
    msgs = [
        {"role": "system", "content": "You are assistant"},
        {"role": "user", "content": "1"},
        {"role": "assistant", "content": "2"},
        {"role": "user", "content": "3"},
        {"role": "assistant", "content": "4"}
    ]
    res = mem.trim(msgs)
    assert len(res) == 4  # 1 system + last 3 messages
    assert res[0]["role"] == "system"
    assert res[-1]["content"] == "4"

if __name__ == '__main__':
    test_memory_trim()
    print("✓ Task 09 passed!")
