from langchain_core.output_parsers import PydanticOutputParser
from src.schemas.common_output_schema import CommonOutputSchema


data_ingestion_parser = PydanticOutputParser(
    pydantic_object=CommonOutputSchema
)

