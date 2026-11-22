from app.graph.state import SupportedState

def classify_intent(state: SupportedState) -> str:
    """
    Classifies the intent of a customer support message based on the provided state.

    Args:
        state (SupportedState): The state containing customer support information.

    Returns:
        str: The classified intent of the message.
    """
    # Example logic for intent classification
    if "refund" in state["message"].lower():
        return "request_refund"
    elif "order status" in state["message"].lower():
        return "check_order_status"
    elif "technical issue" in state["message"].lower():
        return "report_technical_issue"
    else:
        return "general_inquiry"

    return {
        "intent": intent
    }

def route_request(state: SupportedState) -> str:
    """
    Routes the customer support request based on the classified intent.
    Args:
        state (SupportedState): The state containing customer support information.
    Returns:
        str: The routing result or response.
    """
    intent = state["intent"]

    # Example routing logic based on intent
    if intent == "customer_details":
        return "customer"
    elif intent == "order_details":
        return "order"
    elif intent == "payment_status":
        return "payment"
    elif intent == "refund_eligibility":
        return "refund"
    else:
        return "general"