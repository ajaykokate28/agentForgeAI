from typing import Literal

from pydantic import BaseModel

from app.agents.llm_service import get_openai_client
from app.config import settings

class IntentResult(BaseModel):
    intent: Literal[
        "customer_details",
        "order_details",
        "payment_status",
        "refund_eligibility",
        "general_query"
    ]

async def classify_intent_with_llm(message:str) -> str:
    client = get_openai_client()

    response = await client.responses.parse(model=settings.OPENAI_MODEL,
                                            input=[
                                                {
                                                    "role": "system",
                                                    "content": (
                                                        "You are an intent classification system for a customer support application."
                                                        "Classify the customer's message into exactly one category. "
                                                        "order_details: asks about order information, devlivery, tracking, or order status."
                                                        "payment_status: asks whether payment status."
                                                        "refund_eligibility: asks about refunds, returning money, refund eligibility, or refund requests."
                                                        "general_query: greetings, general questions, or requests not covered by the other categories."
                                                        "choose the closest matching category."
                                        
                                                    )
                                                },
                                                {
                                                    "role": "user",
                                                    "content": message
                                                }
                                            ],
                                            text_format= IntentResult
                                            )
    return response.output_parsed.intent
