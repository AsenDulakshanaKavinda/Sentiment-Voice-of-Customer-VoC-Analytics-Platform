import uuid

from langchain.tools import tool

from data_ingestion_service.utils.logger_config import log
from data_ingestion_service.utils.exception_config import ProjectException

@tool
def generate_id():
    """ create a unique id """
    try:
        log.info("ID Generated")
        return uuid.uuid4()
    except Exception as e:
        ProjectException(
            e,
            context={
                "operation": "generate_id",
                "message": "Error generating ID",
            }
        )


