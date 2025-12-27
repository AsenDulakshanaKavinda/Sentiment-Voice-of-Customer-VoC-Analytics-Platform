import json
from data_ingestion_service.utils.logger_config import log
from fastapi import FastAPI, Depends, HTTPException, status

def extract_payload(raw_payload: bytes):
    try:
        payload = json.loads(raw_payload)
        log.info('Extract payload from raw payload')
        return payload
    except Exception as e:
        log.error(e)
        raise HTTPException(status_code=400, detail='Invalid payload')





