import re
from langdetect import detect
import uuid
from datetime import datetime, UTC
import json
import pandas as pd
from sklearn.model_selection import train_test_split

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


def split_data(records: list, filename: str):
    with open(filename, "w") as f:
        json.dump(records, f, indent=4)  
    print(f"Saved {len(records)} records to {filename}")

if __name__ == "__main__":
    data = pd.read_csv("data/test_raw_data/test_raw_data.csv")
    # print(data.head(4))
    results = []
    for raw in data[:10].itertuples():
        result = (preprocess_record(raw.Tweet, "tweetr", raw.Target))
        results.append(result)

    # split into 80/20
    train, temp = train_test_split(results, test_size=0.2, random_state=42)
    # split 10/10 
    val, test = train_test_split(temp, test_size=0.5, random_state=42)


    split_data(train, 'train.json')
    split_data(test, 'test.json')
    split_data(val, 'val.json')

        

    






