from datetime import datetime
from typing import List

_logs: List[dict] = []

def add_log(entry: dict):
    entry["timestamp"] = datetime.utcnow().isoformat()
    _logs.append(entry)
    # Son 50 logu tut
    if len(_logs) > 50:
        _logs.pop(0)

def get_logs() -> List[dict]:
    return list(reversed(_logs))