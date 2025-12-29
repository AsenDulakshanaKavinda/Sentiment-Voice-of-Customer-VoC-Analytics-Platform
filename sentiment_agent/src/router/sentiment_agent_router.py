
from fastapi import APIRouter, Request, Response, HTTPException

from src.agent.sentiment_analytic_agent import sentiment_analytic
from src.utils import log, ProjectException

router = APIRouter()

@router.post('/start')
async def start_sentiment_agent(request: Request):
    try:

        payload = await request.json()
        log.info(f"payload: {payload}")

        log.info("Starting sentiment agent")
        result = sentiment_analytic(payload)

        log.info(f"Sentiment agent result: {result}")

        return {
            "status": "success",
            "statusCode": 200,
            "message": "sentiment agent started",
        }
    except Exception as e:
        log.error(e)
        raise HTTPException(status_code=500, detail=str(e))















