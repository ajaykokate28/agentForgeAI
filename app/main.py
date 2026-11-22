from fastapi import FastAPI
from app.api.routes.support import router as support_router

app = FastAPI(
    title="AgentForge AI",
    description="Multi-Agent Customer Support System",
    version="1.0.0"
)

@app.get("/")
async def home():
    return {
        "application": "AgentForge AI",
        "message": "Welcome to the AgentForge AI API",
        "status": "running"
         }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }

app.include_router(
    support_router,
    prefix="/api/v1/support",
    tags=["Customer Support"]
)    