from langchain_core.output_parsers import PydanticOutputParser

from src.schemas.sentiment_schema import SentimentAgentOutput

sentiment_agent_parser = PydanticOutputParser(
    pydantic_object=SentimentAgentOutput
)


