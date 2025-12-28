
from fastapi import APIRouter, Request, Response, HTTPException

from sentiment_agent.utils.logger_config import log


router = APIRouter()

@router.post('/start')
async def start_sentiment_agent(request: Request):
    try:
        log.info("Starting sentiment agent")
        return {
            "status": "success",
            "statusCode": 200,
            "message": "sentiment agent started",
        }
    except Exception as e:
        log.error(e)
        raise HTTPException















