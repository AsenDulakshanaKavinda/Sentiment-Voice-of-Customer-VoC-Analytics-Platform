import json
from src.utils import log, ProjectException
from fastapi import FastAPI, Depends, HTTPException, status

def extract_payload(raw_payload: bytes):
    try:
        payload = json.loads(raw_payload)
        log.info('Extract payload from raw payload')
        return payload
    except Exception as e:
        log.error(e)
        raise HTTPException(status_code=400, detail='Invalid payload')





