from deep_translator import GoogleTranslator
from langchain.tools import tool
import pycld2 as cld2
import nltk

from data_ingestion_service.utils.logger_config import log
from data_ingestion_service.utils.exception_config import ProjectException

try:
    nltk.download('punkt', quiet=True)
    nltk.download('punkt_tab', quiet=True)
except Exception as e:
    log.error(f'--------------------------------{str(e)}')




# @tool
def detect_language_translate(text: str):
    """Detects languages in the provided text, which may contain segments in multiple languages.
    Returns a structured dictionary where keys are text segments and values include the language name and code."""

    # if there is no text to translate return {}
    if not text:
        log.warning("No text provided for `detect_language` tool...")
        return {}

    try:
        extract_sentences = {}

        is_reliable, text_bytes_found, details, vectors = cld2.detect(text, returnVectors=True)

        # Correct extraction using byte slicing
        text_bytes = text.encode('utf-8')
        for offset, length, lang_name, lang_code in vectors:
            segment_bytes = text_bytes[offset:offset + length]
            segment = segment_bytes.decode('utf-8')

            if not segment:
                log.info("No segment found for `detect_language` tool...")
                continue
            supported_langs = ['en', 'fr', 'de']
            sentences = nltk.sent_tokenize(segment, language=lang_code.lower() if lang_code.lower() in supported_langs else 'english')

            translator = GoogleTranslator(source='auto', target='en')
            translated_sentences = translator.translate_batch(sentences)

            extract_sentences[segment] = {
                "original_sentences": sentences,
                "translated_sentences": translated_sentences,
            }

            log.info(f"Segment: {segment[:10]}, detect language{lang_name}, translated sentence: {translated_sentences[:10]}")

        return extract_sentences
    except Exception as e:
        ProjectException(
            e,
            context={"operation": "detect_language", "text": text},
        )



if __name__ == '__main__':
    # uncomment if only need to test the `detect_language` function
    text = "Bonjour le monde! Ceci est une phrase en français. හල වර්ගය. நான் உன்னை காதலி்கிறேன்"
    extract_sentences = detect_language_translate(text)
    print(extract_sentences)




