
import os
from dotenv import load_dotenv; load_dotenv()

from langchain_mistralai import ChatMistralAI

from src.agent.tools import detect_language_translate, expand_slang, clean_and_anonymize_text, generate_id, generate_timestamp

from src.utils import log, ProjectException


os.environ["MISTRAL_API_KEY"]=os.getenv("MISTRAL_API_KEY")

def load_model():
    """ Load the LLM for Data Ingestion Service and bind the tools to the LLM """
    try:
        model = ChatMistralAI(
            model_name="mistral-large-latest"
        )
        log.info("model loaded")
        model_with_tools = model.bind_tools([generate_id, generate_timestamp, detect_language_translate, 
                                             expand_slang, clean_and_anonymize_text])
        log.info("Model loaded with tools...")
        return model_with_tools
    except Exception as e:
        ProjectException(
            e,
            context={
                "operation": "load_model",
                "message": "Failed to load model",
            }
        )

loaded_model_with_tools = load_model()



