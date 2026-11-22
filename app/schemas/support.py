from pydantic import BaseModel, Field

class SupportRequest(BaseModel):
    customer_id: int = Field(gt=0)
    message: str = Field(min_length=5, max_length=5000)

class SupportResponse(BaseModel):
    customer_id: int
    status: str
    message: str