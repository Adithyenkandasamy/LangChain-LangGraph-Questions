"""
PRACTICAL CHALLENGE: Agent Graph Streaming Event Streamer (LC-H7-P14)
=====================================================
ID: LC-H7-P14
Curriculum Tier: Mastery | Focus: Autonomous LangGraph RAG Agent
Task:
Implement `parse_agent_events(events)` generator that categorizes events into
`node_start`, `tool_call`, `token`, and `node_end`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def parse_agent_events(events: list):
    parsed = []
    for ev in events:
        ev_type = ev.get("event")
        if ev_type == "on_chat_model_stream":
            parsed.append({"type": "token", "data": ev.get("data", {}).get("chunk", "")})
        elif ev_type == "on_tool_start":
            parsed.append({"type": "tool_call", "tool": ev.get("name")})
        elif ev_type == "on_chain_end":
            parsed.append({"type": "node_end", "output": ev.get("data", {}).get("output")})
    return parsed

def test_event_parser():
    raw_events = [
        {"event": "on_tool_start", "name": "vector_search"},
        {"event": "on_chat_model_stream", "data": {"chunk": "Hello"}},
        {"event": "on_chain_end", "data": {"output": "Done"}}
    ]
    parsed = parse_agent_events(raw_events)
    assert len(parsed) == 3
    assert parsed[0]["type"] == "tool_call"
    assert parsed[1]["type"] == "token"
    assert parsed[2]["type"] == "node_end"

if __name__ == '__main__':
    test_event_parser()
    print("✓ Task 14 passed!")
