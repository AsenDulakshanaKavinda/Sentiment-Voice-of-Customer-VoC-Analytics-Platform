import re

from langsmith import expect

from data_ingestion_service.utils.logger_config import log
from data_ingestion_service.utils.exception_config import ProjectException
from langchain.tools import tool

@tool
def clean_and_anonymize_text(text):
    """
    Removes noise (HTML tags, emojis, URLs as potential spam) and anonymizes PII (emails, phone numbers).

    - HTML: Strips tags like <div> or <a href="...">.
    - Emojis: Removes Unicode emoji characters.
    - Spam/Noise: Removes URLs (e.g., http://example.com) as they often indicate spam.
    - PII Anonymization: Replaces emails with [EMAIL] and phone numbers with [PHONE].
      - Emails: Matches common formats like user@example.com.
      - Phones: Matches common formats like (123) 456-7890, 123-456-7890, or +1-123-456-7890 (supports international prefixes).

    Returns the cleaned text.
    """
    if not text:
        log.warning("Empty text, nothing to anonymize and clean...")
        return ""


    try:
        # Remove HTML tags
        text = re.sub(r'<[^>]*>', '', text)

        # Remove emojis (Unicode ranges for common emojis)
        emoji_pattern = re.compile(
            r'[\U0001F600-\U0001F64F'  # Emoticons
            r'\U0001F300-\U0001F5FF'  # Symbols & pictographs
            r'\U0001F680-\U0001F6FF'  # Transport & map symbols
            r'\U0001F700-\U0001F77F'  # Alchemical symbols
            r'\U0001F780-\U0001F7FF'  # Geometric shapes extended
            r'\U0001F800-\U0001F8FF'  # Supplemental arrows
            r'\U0001F900-\U0001F9FF'  # Supplemental symbols
            r'\U0001FA00-\U0001FA6F'  # Chess symbols
            r'\U0001FA70-\U0001FAFF'  # Symbols and pictographs extended
            r'\U00002702-\U000027B0'  # Dingbats
            r'\U000024C2-\U0001F251'  # Enclosed characters
            r']+', flags=re.UNICODE
        )
        text = emoji_pattern.sub('', text)

        # Remove URLs (potential spam)
        text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)

        # Anonymize emails
        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        text = email_pattern.sub('[EMAIL]', text)

        # Anonymize phone numbers (supports various formats, including international)
        phone_pattern = re.compile(
            r'(?:(?:\+?(\d{1,3}))?[-. (]*(\d{3})?[-. )]*(\d{3})?[-. ]*(\d{4})?\b)'
        )
        text = phone_pattern.sub('[PHONE]', text)

        # Clean up extra whitespace
        text = ' '.join(text.split())

        log.info("Cleaning text...")
        return text
    except Exception as e:
        ProjectException(
            e,
            context={
                "operation": "clean_and_anonymize_text",
                "message": "Error while cleaning the text"
            }
        )


