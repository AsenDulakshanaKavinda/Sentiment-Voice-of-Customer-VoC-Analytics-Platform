
from langchain.tools import tool
import pycld2 as cld2

from data_ingestion_service.utils.logger_config import log
from data_ingestion_service.utils.exception_config import ProjectException

@tool
def detect_language(text: str):
    """Detects languages in the provided text, which may contain segments in multiple languages.
    Returns a structured dictionary where keys are text segments and values include the language name and code."""
    extract_sentences = {}

    if not text:
        log.warning("No text provided for `detect_language` tool...")
        return {}

    try:
        is_reliable, text_bytes_found, details, vectors = cld2.detect(text, returnVectors=True)

        # Correct extraction using byte slicing
        text_bytes = text.encode('utf-8')
        for offset, length, lang_name, lang_code in vectors:
            segment_bytes = text_bytes[offset:offset + length]
            segment = segment_bytes.decode('utf-8')

            extract_sentences[segment] = {
                "language": lang_name,
                "language_code": lang_code,
            }

            log.info(f"Segment: {segment[:10]}, detect language{lang_name}")

        return extract_sentences
    except Exception as e:
        ProjectException(
            e,
            context={"operation": "detect_language", "text": text},
        )



if __name__ == '__main__':
    # uncomment if only need to test the `detect_language` function
    # text = "Bonjour le monde! Ceci est une phrase en français. හල වර්ගය. நான் உன்னை காதலி்கிறேன்"
    # extract_sentences = detect_language(text)
    # print(extract_sentences)




