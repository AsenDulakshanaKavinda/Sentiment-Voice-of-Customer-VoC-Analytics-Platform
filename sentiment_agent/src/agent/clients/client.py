import os
from dotenv import load_dotenv; load_dotenv()

from langchain_mistralai import ChatMistralAI

from src.utils import log, ProjectException

os.environ["MISTRAL_API_KEY"]=os.getenv("MISTRAL_API_KEY")

from src.utils.project_config import project_config


def load_model():
    """ Load and return the LLM use in Sentiment Analysis Agent """


    try:
        llm_config = project_config['LLM']
        log.info(f'llm_config: {llm_config}')
        if not llm_config:
            raise KeyError('Missing `LLM` section in config')
        
        model_name = llm_config.get('model_name')
        if not model_name:
            raise ValueError("Missing `model_name` under LLM in config")


        model = ChatMistralAI(
            model_name=project_config['LLM']['model_name']
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














