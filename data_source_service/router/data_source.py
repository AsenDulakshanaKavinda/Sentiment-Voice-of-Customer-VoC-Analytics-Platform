
import os
from pathlib import Path
from dotenv import load_dotenv; load_dotenv()

from fastapi import APIRouter

from data_source_service.handlers.call_logs_handler import handle_call_logs





router = APIRouter()
@router.post("/start")
def handle_call_logs_endpoint():
    call_log_filepath = Path(os.getenv("CALL_LOG_FILEPATH"))
    if not call_log_filepath:
        raise RuntimeError(
            "CALL_LOG_FILEPATH environment variable is not set"
        )
    handle_call_logs(filepath=call_log_filepath)






