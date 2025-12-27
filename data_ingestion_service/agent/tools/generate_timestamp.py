from datetime import datetime

from langchain.tools import tool

from data_ingestion_service.utils.logger_config import log
from data_ingestion_service.utils.exception_config import ProjectException

@tool
def generate_timestamp():
    """  """
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






