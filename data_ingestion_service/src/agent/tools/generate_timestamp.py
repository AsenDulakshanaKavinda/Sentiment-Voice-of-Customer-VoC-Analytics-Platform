from datetime import datetime, timezone

from langchain.tools import tool

from src.utils import log, ProjectException

@tool
def generate_timestamp():
    """ Generate the timestamp Data Ingestion """
    try:
        log.info("Generating timestamp")
        return datetime.now(timezone.utc).isoformat()
    except Exception as e:
        ProjectException(
            e,
            context={
                "operation": "generate_timestamp",
                "message": "failed to generate timestamp",
            }
        )






