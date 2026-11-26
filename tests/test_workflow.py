from app.graph.workflow import build_support_graph

def test_build_support_graph():
    graph = build_support_graph()

    initial_state = {
        "customer_id": 12345,
        "message": "I need help with my account.",
        "intent": "",
        "order_id": "ORD-10001",
        "tool_result": {},
        "final_response": ""
    }

    result = graph.invoke(initial_state)

    assert result["intent"] == "general_inquiry"

def test_customer_workflow_returns_customer_details():
    graph = build_support_graph()

    initial_state = {
        "customer_id": 12345,
        "message": "I need help with my account.",
        "intent": "",
        "order_id": "ORD-10001",
        "tool_result": {},
        "final_response": ""
    }

    result = graph.invoke(initial_state)

    assert result["intent"] == "customer_details"
    assert result["tool_result"]["found"] is True
    assert result["tool_result"]["customer"]["name"] == "john"
    assert "Rahul" in result["final_response"]

def test_general_query_workflow():
    graph = build_support_graph()

    initial_state = {
        "custmer_id": 101,
        "message": "Hello, how can you help me?",
        "intent": "",
        "order_id": "",
        "tool_result": {},
        "final_response": ""
    }

    result = graph.invoke(initial_state)
    assert "customer support" in result["final_response"].lower()
