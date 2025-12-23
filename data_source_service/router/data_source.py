
import os
from pathlib import Path
from dotenv import load_dotenv; load_dotenv()

from fastapi import APIRouter

from data_source_service.handlers.source_handler import handle_source

router = APIRouter()
@router.post("/start")
def handle_logs_endpoint():

    """ Read all the source files, and handle logs.(send to other services) """

    source_files = ['call_center_transcripts', 'chat_transcripts', 'emails', 'product_reviews', 'social_media', 'support_tickets'] # source files
    data_dir = Path(os.getenv("SOURCE_FILEPATH"))

    for source_file in source_files:
        file_path = data_dir / f"{source_file}.json"
        if file_path.exists():
            handle_source(file_path)
            return {"status": "success", "message": f"{source_file}logs senf successfully."}
        return {"status": "error", "message": f"{source_file}logs failed to send."}
    return {"status": "read the source"}






