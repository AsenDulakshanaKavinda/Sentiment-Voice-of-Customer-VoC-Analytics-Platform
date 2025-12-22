import os
from pathlib import Path
from dotenv import load_dotenv; load_dotenv()



FILEPATH = Path(os.getenv("CALL_LOG_FILEPATH"))
print(FILEPATH)