

from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from sentiment_agent.router.sentiment_agent_router import router
from sentiment_agent.middleware.log_middleware import log_middleware


app = FastAPI(
    title="Sentiment Analytics Service Of the Customer Analytics Platform",
    description="This work as the sentiment analytic agent and analyze the customer feedbacks",
    version="1.0.0",
    docs_url="/docs",
)

# middleware
app.add_middleware(
    BaseHTTPMiddleware, dispatch=log_middleware
)


@app.get("/", description="Root URL")
async def root():
    return {"message": "Welcome to Sentiment Agent Service of the Voice Of Customer Analytics Platform's 'Data Source Service'! "
                       "Visit /docs for the API documentation."}


app.include_router(
    router,
    prefix="/sentiment_agent",
    tags=["sentiment_agent"]
)









