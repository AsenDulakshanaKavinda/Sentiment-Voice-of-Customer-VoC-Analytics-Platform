
import os
from dotenv import load_dotenv; load_dotenv()



from langchain_mistralai import ChatMistralAI

from data_ingestion_service.agent.tools.language_detector import detect_language_translate
from data_ingestion_service.agent.tools.handle_slang import expand_slang
from data_ingestion_service.agent.tools.clean_and_anonymize import clean_and_anonymize_text
from data_ingestion_service.schemas.common_output_schema import CommonOutputSchema

from data_ingestion_service.utils.exception_config import ProjectException
from data_ingestion_service.utils.logger_config import log

os.environ["MISTRAL_API_KEY"]=os.getenv("MISTRAL_API_KEY")

def load_model():
    try:
        model = ChatMistralAI(
            model_name="mistral-large-latest"
        )
        log.info("model loaded")
        model_with_tools = model.bind_tools([detect_language_translate, expand_slang, clean_and_anonymize_text])
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



