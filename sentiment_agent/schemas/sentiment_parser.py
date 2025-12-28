from langchain_core.output_parsers import PydanticOutputParser
from sentiment_agent.schemas.sentiment_schema import SentimentAgentOutput

sentiment_agent_parser = PydanticOutputParser(
    pydantic_object=SentimentAgentOutput
)


