from fastapi import APIRouter, Request, Depends, HTTPException
from data_ingestion_service.utils.logger_config import log

from data_ingestion_service.router.ingestion_helper import extract_payload


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
        return {
            "status": "success",
            "statusCode": 200,
            "message": "payload received and logged",
        }
    except Exception as e:
        log.error(f"error processing payload: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))







