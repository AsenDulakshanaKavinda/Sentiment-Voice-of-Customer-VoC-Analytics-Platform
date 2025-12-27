from langchain_core.output_parsers import PydanticOutputParser
from data_ingestion_service.schemas.common_output_schema import CommonOutputSchema

data_ingestion_parser = PydanticOutputParser(
    pydantic_object=CommonOutputSchema
)

