from app.graph.state import SupportedState

from app.tools.customer_tools import (get_order_details, get_customer_details,  check_payment_status, check_refund_eligibility)

from app.agents.intent_classifier import classify_intent_with_llm

async def classify_intent(state: SupportedState) -> dict:

    message = state["message"]

    intent = await classify_intent_with_llm(message)
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

def handle_order_request(state: SupportedState) -> str:
   order_id = state["order_id"]

   result = get_order_details(order_id)

   if result["found"]:
       order = result["order"]

       response = (f"Your order {order_id} is for {order['product']}. " f"The status is {order['order_status']}.")
   else:
        response = result["message"]

   return {
       "tool_result": result,
       "final_response": response
   }

def handle_payment_request(state: SupportedState) -> str:
    order_id = state["order_id"]

    result = check_payment_status(order_id)

    if result["found"]:
        payment = result["payment"]

        response = (
            f"The payment for order {order_id} is {payment['status']}. "
            f"The amount paid is {payment['amount']}."
        )
    else:
        response = result["message"]

    return {
        "tool_result": result,
        "final_response": response
    }

def handle_refund_request(state: SupportedState) -> dict:
    order_id = state["order_id"]

    result = check_refund_eligibility(order_id)

    if result["eligible"]: response =( f"Your order {order_id} is eligible for a refund."
                                      f"Eligible refund amount: Rs. {result['refund_amount']}."
                                      "Please note that the refund has not been processed yet.")
    else: response = (f"Your order {order_id} is not eligible for a refund. "
                      f"Reason: {result['reason']}")
    return {
        "tool_result": result,
        "final_response": response         
         }

def handle_general_request(state: SupportedState) -> dict:
    message = state["message"]

    response = (
        "Thank you for contacting customer support."
        "I can help you with customer details, order information, "
        "payment status, and refund eligibility. "
        "Please share more details about your issue."
    )

    return {
        "tool_result": {},
        "final_response": response
    }