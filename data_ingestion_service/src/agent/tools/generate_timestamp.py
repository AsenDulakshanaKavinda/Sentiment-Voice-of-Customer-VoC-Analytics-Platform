from datetime import datetime

from langchain.tools import tool

from src.utils import log, ProjectException

@tool
def generate_timestamp():
    """ Generate the timestamp Data Ingestion """
    try:
        log.info("Generating timestamp")
        return datetime.now()
    except Exception as e:
        ProjectException(
            e,
            context={
                "operation": "generate_timestamp",
                "message": "failed to generate timestamp",
            }
        )






