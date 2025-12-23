
from fastapi import FastAPI, Request, Response
from data_source_service.router.data_source import router
from data_source_service.middleware.log_middleware import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware
from data_source_service.utils.logger_config import log

app = FastAPI(
    title="Data Source Service of the Voice Of Customer Analytics Platform",
    description="This service handle the data by sending data to other services according to the data platform that data provide",
    version="1.0.0",
    docs_url="/docs"
)

# middleware
app.add_middleware(
    BaseHTTPMiddleware, dispatch=log_middleware,
)

@app.get("/", description='Root')
async def root():
    return {"message": "Welcome to Service of the Voice Of Customer Analytics Platform's 'Data Source Service'! Visit /docs for the API documentation."}

app.include_router(
    router,
    prefix="/data_source",
    tags=["data_source"]
)