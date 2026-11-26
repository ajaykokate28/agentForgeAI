import asyncio
from app.graph.nodes import classify_intent, route_request

def test_classify_intent(monkeypatch):
    async def fake_classify_intent(message: str) -> str:
        return "order_details"

    monkeypatch.setattr(
        "app.graph.nodes.classify_intent_with_llm",
        fake_classify_intent,
    )
    # Test case 1: Refund request
    state = {
        "customer_id": 1,
        "message": "I would like to request a refund for my order.",
        "intent": "",
        "order_id": "12345",
        "tool_result": {},
        "final_response": ""
    }
    result = asyncio.run(classify_intent(state))
    assert result["intent"]== "order_details"

 
def test_route_order_request():
    state = {
        "customer_id": 101,
        "message": "Where is my order?",
        "intent": "order_details",
        "order_id": "ORD-1001",
        "tools_result": {},
        "final_response": ""
    }

    result = route_request(state)
    assert result == "order"