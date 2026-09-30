"""
PRACTICAL CHALLENGE: add_messages Reducer Logic (LC-H5-P08)
=====================================================
ID: LC-H5-P08
Curriculum Tier: Advanced | Focus: Tool Calling & LangGraph Basics
Task:
Implement the `add_messages(existing_messages, new_messages)` reducer logic that appends
messages or updates an existing message if their IDs match.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def add_messages(existing: list, new_msgs: list) -> list:
    result = list(existing)
    id_to_index = {m.get("id"): idx for idx, m in enumerate(result) if "id" in m}

    for msg in new_msgs:
        m_id = msg.get("id")
        if m_id and m_id in id_to_index:
            result[id_to_index[m_id]] = msg
        else:
            result.append(msg)
            if m_id:
                id_to_index[m_id] = len(result) - 1
    return result

def test_add_messages_reducer():
    base = [{"id": "1", "content": "Hello"}]
    # Append new message
    res1 = add_messages(base, [{"id": "2", "content": "Hi"}])
    assert len(res1) == 2

    # Update existing message with matching id
    res2 = add_messages(res1, [{"id": "1", "content": "Updated Hello"}])
    assert len(res2) == 2
    assert res2[0]["content"] == "Updated Hello"

if __name__ == '__main__':
    test_add_messages_reducer()
    print("✓ Task 08 passed!")
