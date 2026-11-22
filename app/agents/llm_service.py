from functools import lru_cache
from openai import AsyncOpenAI
from app.config import Settings

@lru_cache()
def get_openai_client() -> AsyncOpenAI:
    if not Settings.OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

    return AsyncOpenAI(api_key=Settings.OPENAI_API_KEY, model=Settings.OPENAI_MODEL)    

async def generate_support_reply(customer_message: str) -> str:
    """
    Generate a support reply using the OpenAI API based on the customer's message.
    """
    client = get_openai_client()
    
    prompt = f"Customer message: {customer_message}\n\nGenerate a helpful and professional support reply."
    
    response = await client.responses.create(
        model= Settings.OPENAI_MODEL,
        instructions="""You are a professional customer support assistant.
        
        Your responsibilities:
        1. Understand the customer's message and context.
        2. Generate a clear, concise, and helpful response.
        3. Maintain a polite and professional tone.
        4. Avoid using any personal information or sensitive data in your response.
        5. Ensure the response is relevant to the customer's inquiry and provides actionable advice or solutions.
        """,
        input = customer_message
    )
    
    return response.output_text