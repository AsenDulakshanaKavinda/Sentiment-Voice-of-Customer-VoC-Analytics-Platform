
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from data_ingestion_service.router.data_ingestion import router
from data_ingestion_service.middleware.log_middleware import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI(
    title="Data Ingestion Service of the Voice Of Customer Analytics Platform",
    description="This service handle the data by cleaning and reorganize to a common schema.",
    version="1.0.0",
    docs_url="/docs",
)

# middleware
app.add_middleware(
    BaseHTTPMiddleware, dispatch=log_middleware
)

@app.get("/", description='Root URL')
async def root():
    return {"message": "Welcome to Data Ingestion Service of the Voice Of Customer Analytics Platform's 'Data Source Service'! Visit /docs for the API documentation."}

app.include_router(
    router,
    prefix="/data_ingestion",
    tags=["data_ingestion"],
)