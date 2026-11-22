from app.graph.nodes import classify_intent, route_request

def test_classify_intent():
    # Test case 1: Refund request
    state = {
        "customer_id": 1,
        "message": "I would like to request a refund for my order.",
        "intent": "",
        "order_id": "12345",
        "tool_result": {},
        "final_response": ""
    }
    assert classify_intent(state) == "request_refund"

    # Test case 2: Order status inquiry
    state["message"] = "Can you provide the status of my order?"
    assert classify_intent(state) == "check_order_status"

    # Test case 3: Technical issue report
    state["message"] = "I'm experiencing a technical issue with the product."
    assert classify_intent(state) == "report_technical_issue"

    # Test case 4: General inquiry
    state["message"] = "I have a question about your services."
    assert classify_intent(state) == "general_inquiry"
 
def test_route_order_request():
    state = {
        "intent": "order_details"
    }

    result = route_request(state)
    assert result == "order"