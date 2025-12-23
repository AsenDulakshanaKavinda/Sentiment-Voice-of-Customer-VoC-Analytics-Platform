

import json
from pathlib import Path


from data_source_service.clients.call_logs_client import send_to_ingestor

def handle_source(filepath: Path) -> None:
    """ Read all the source files, and handle logs.(send to other services) """
    try:
        with open(filepath) as json_file:
            logs = json.load(json_file)

        if logs:
            for log in logs:
                send_to_ingestor(log)
            print(f"read: {len(logs)} logs")
        else:
            print("no logs")


    except FileNotFoundError as e:
        print(f'File not found: {e}')
    except json.JSONDecodeError as e:
        print(f'JSON decode error: {e}')


if __name__ == '__main__':
    filepath = Path(__file__).resolve().parent / 'chat_transcripts.json'
    handle_source(filepath)










