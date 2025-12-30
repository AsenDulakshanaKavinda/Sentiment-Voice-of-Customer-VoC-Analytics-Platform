from fastapi import APIRouter, Request, Depends, HTTPException
from src.utils import log, ProjectException

from src.router.ingestion_helper import extract_payload
from src.agent.ingestion_agent import ingest_logs


router = APIRouter()


@router.post('/start')
async def start_ingestion(request: Request):
    try:
        payload = await request.json()

        # to-dos
        # - 1. Remove noise (HTML, emojis, spam) - use `re`
        # - 2. Anonymize PII (emails, phone numbers)
        # - 2. Language detection - `pycld2' - `re`
        # - 4. Translate to a common language - `googletrans`
        # - 5. Handle slang, abbreviations - `re`
        
        log.info(f"payload: {payload}")

        result = ingest_logs(payload)
        log.info("Invoking data ingestion complete...")

        # todo - send result to sentiment analyze

        return {
            "status": "success",
            "statusCode": 200,
            "message": "payload received and Ingested",
        }
    except Exception as e:
        log.error(f"error processing payload: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))







