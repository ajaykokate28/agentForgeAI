from app.graph.workflow import build_support_graph

def test_build_support_graph():
    graph = build_support_graph()

    initial_state = {
        "customer_id": "12345",
        "message": "I need help with my account.",
        "intent": None,
        "order_id": "ORD-10001",
        "tool_result": {},
        "final_response": ""
    }

    result = graph.invoke(initial_state)

    assert result["intent"] == "order_details"  # Assuming the intent classification returns "order_details"