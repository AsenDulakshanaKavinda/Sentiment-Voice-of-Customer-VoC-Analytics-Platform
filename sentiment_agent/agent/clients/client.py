import os
from dotenv import load_dotenv; load_dotenv()

from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistralAI

from sentiment_agent.utils.logger_config import log
from sentiment_agent.utils.exception_config import ProjectException

os.environ["MISTRAL_API_KEY"]=os.getenv("MISTRAL_API_KEY")


def load_model():
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














