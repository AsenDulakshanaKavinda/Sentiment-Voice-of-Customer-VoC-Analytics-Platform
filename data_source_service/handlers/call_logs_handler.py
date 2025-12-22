

import json
from pathlib import Path


from data_source_service.clients.call_logs_client import senf_to_ingestor

def handle_call_logs(filepath: Path) -> None:
    try:
        with open(filepath) as json_file:
            logs = json.load(json_file)

        if logs:
            for log in logs:
                senf_to_ingestor(log)
            print(f"read: {len(logs)} logs")
        else:
            print("no logs")


    except FileNotFoundError as e:
        print(f'File not found: {e}')
    except json.JSONDecodeError as e:
        print(f'JSON decode error: {e}')


if __name__ == '__main__':
    filepath = Path(__file__).resolve().parent / 'call_logs.json'
    handle_call_logs(filepath)










