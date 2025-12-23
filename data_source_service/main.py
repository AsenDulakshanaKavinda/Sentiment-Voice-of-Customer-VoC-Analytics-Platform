
from fastapi import FastAPI, Request, Response
from data_source_service.router.data_source import router

from data_source_service.utils.logger_config import log

app = FastAPI(
    title="Data Source Service of the Voice Of Customer Analytics Platform",
    description="This service handle the data by sending data to other services according to the data platform that data provide",
    version="1.0.0",
    docs_url="/docs"
)

@app.middleware("http")
async def middleware(request: Request, call_next):
    log_dict = {
        'url': request.url.path,
        'method': request.method,
    }
    log.info(log_dict)

    response = await call_next(request)
    return response

@app.get("/")
async def root():
    return {"message": "Welcome to Service of the Voice Of Customer Analytics Platform's 'Data Source Service'! Visit /docs for the API documentation."}

app.include_router(
    router,
    prefix="/data_source",
    tags=["data_source"]
)



