from fastapi import APIRouter, HTTPException

from openai import APIError, RateLimitError

from app.agents.llm_service import generate_support_reply
from app.schemas.support import (
    SupportRequest,
    SupportResponse
)

router = APIRouter()

@router.post("/messages", response_model=SupportResponse)

async def receive_customer_message(
    request: SupportRequest
    ):
    try:
        ai_reply = await generate_support_reply(request.message)
        return SupportResponse(
            message= ai_reply,
            status= "success"
        )
    except RateLimitError:
        raise HTTPException(status_code=429, detail="Rate limit exceeded. Please try again later.")
    except APIError:
        # Handle API errors appropriately
        raise HTTPException(status_code=502, detail="Failed to process support request")