from datetime import datetime, timezone

from langchain.tools import tool

from data_ingestion_service.utils.logger_config import log
from data_ingestion_service.utils.exception_config import ProjectException

@tool
def generate_timestamp():
    """"
    Generate a timestamp representing when the data ingestion process occurs.
    This tool is intended to be used within a LangChain pipeline to provide
    a consistent ingestion-time marker for records, logs, or metadata.
    It captures the current system time at the moment the tool is invoked.
    """

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






