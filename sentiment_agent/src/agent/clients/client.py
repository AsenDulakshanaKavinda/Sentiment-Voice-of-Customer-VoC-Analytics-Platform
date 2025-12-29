import os
from dotenv import load_dotenv; load_dotenv()

from langchain_mistralai import ChatMistralAI

from src.utils import log, ProjectException


os.environ["MISTRAL_API_KEY"]=os.getenv("MISTRAL_API_KEY")


def load_model():
    """ Load and return the LLM use in Sentiment Analysis Agent """


    try:
        model = ChatMistralAI(
            model_name="mistral-large-latest"
        )
        log.info("model loaded - sentiment")
        return model
    except Exception as e:
        ProjectException(
            e,
            context={
                "operation": "load sentiment model",
                "message": "Failed to load model",
            }
        )


sentiment_model = load_model()














