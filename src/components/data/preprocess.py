import re
from langdetect import detect
import uuid
from datetime import datetime, UTC

PII_PATTERNS = [
    (re.compile(r"\b[\w.-]+?@\w+?\.\w{2,4}\b"), "[EMAIL]"),
    (re.compile(r"\b(?:\+?\d{1,3})?[-.\s]?(?:\d{2,4}[-.\s]?){2,}\d{2,4}\b"), "[PHONE]"),
    (re.compile(r'https?://\S+|www\.\S+'), "[URL]"),
    (re.compile(r"@\w+"), "[USER]"),
    (re.compile(r"#\w+"), "[HASHTAG]"),
    (re.compile(r"\d+"), "[NUMBER]"),
]

def redact_pii(text: str) -> str:
    for r, token in PII_PATTERNS:
        text = r.sub(token, text)
    return text

def simple_clean(text: str) -> str:
    text = text.replace("\n", " ").strip() # replace new line with " "
    text = re.sub(r"\s+", " ", text) # whitespace to " "
    return text

def preprocess_record(raw_text: str, source='unknown', label=None) -> dict:
    text = redact_pii(raw_text)
    text = simple_clean(text)

    try:
        lang = detect(text)
    except Exception:
        lang = 'unknown' 
    rec = {
        "id": str(uuid.uuid4()),
        "source": source,
        "text": raw_text,
        "clean_text": text.lower(),
        "lang": lang,
        "sentiment": None if label is None else ("negative" if label == 0 else "positive"),
        "label": label,
        "timestamp": datetime.now(UTC).strftime('%Y-%m-%dT%H:%M:%SZ'),
        "metadata": {}
    }
    return rec

if __name__ == "__main__":
    pass




