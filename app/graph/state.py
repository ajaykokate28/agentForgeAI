from typing import TypedDict

class SupportedState(TypedDict):
    customer_id: int
    message: str
    intent: str
    order_id: str
    tool_result: dict
    final_response: str