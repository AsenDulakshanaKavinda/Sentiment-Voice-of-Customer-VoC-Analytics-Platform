
import os

import requests
from dotenv import load_dotenv; load_dotenv()

from data_source_service.schemas.call_logs import CallLogOut

LOGS_URL = os.getenv("LOGS_URL")

def send_to_ingestor(payload: CallLogOut):
    """ Send a call to the ingestor. """
    response = requests.post(LOGS_URL, json=payload)
    response.raise_for_status()







