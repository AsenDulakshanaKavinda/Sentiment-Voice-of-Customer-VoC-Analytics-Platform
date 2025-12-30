import uuid

from langchain.tools import tool

from src.utils import log, ProjectException

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


