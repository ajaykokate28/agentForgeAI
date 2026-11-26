from langgraph.graph import StateGraph, START, END
from app.graph.state import SupportedState
from app.graph.nodes import (classify_intent, route_request, get_customer_details, 
                             handle_order_request, handle_payment_request, handle_refund_request,
                               handle_general_request)

def build_support_graph():

    # Create the graph
    builder = StateGraph(SupportedState)

    # Register the classification node
    builder.add_node("classify_intent", lambda state: {"intent": classify_intent(state)})

    # Register the routing node
    builder.add_node("customer", handle_customer_request)
    builder.add_node("order", handle_order_request)
    builder.add_node("payment", handle_payment_request)
    builder.add_node("refund", handle_refund_request)
    builder.add_node("general", handle_general_request)

    # Connect START to classification
    builder.add_edge(START, "classify_intent")

    # Define conditional routing
    builder.add_conditional_edges("classify_intent",
        route_request,
        {
            "customer": "customer",
            "order": "order",
            "payment": "payment",
            "refund": "refund",
            "general": "general"
        }
    )

    # Connect handler nodes to the END
    builder.add_edge("customer", END)
    builder.add_edge("order", END)
    builder.add_edge("payment", END)
    builder.add_edge("refund", END)
    builder.add_edge("general", END)

    # Compile the graph
    graph = builder.compile()

    return graph

def handle_customer_request(state: SupportedState) -> dict:
    customer_id = state["customer_id"]

    result = get_customer_details(customer_id)

    if result["found"]:
        customer = result["customer"]

        response = (
            f"Hello {customer['name']}, "
            f"your registered email is {customer['email']}. "
            f"Your membership is {customer['membership']}."        
        )
    else:
        response = result["message"]

    return {
        "tool_result": result,
        "final_response": response
    }

