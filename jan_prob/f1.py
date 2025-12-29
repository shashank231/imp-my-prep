from dataclasses import dataclass
from collections import defaultdict, Counter
from typing import Dict, List, Any
import json
from pathlib import Path

@dataclass
class LogEvent:
    timestamp: str
    user_id: str
    action: str
    status: str

def parse_line(line: str) -> LogEvent | None:
    """Parse single line, return None on error."""
    parts = line.strip().split('|')
    if len(parts) != 4:
        return None
    return LogEvent(*parts)

def process_log_file(filepath: str) -> Dict[str, Any]:
    """Main orchestrator: read, parse, aggregate."""
    if not Path(filepath).exists():
        raise FileNotFoundError(f"File {filepath} not found")
    
    users_by_action = defaultdict(set)
    user_event_counts = Counter()

    with open(filepath, 'r') as f:
        for line_num, line in enumerate(f, 1):
            event = parse_line(line)
            if event:
                users_by_action[event.action].add(event.user_id)
                user_event_counts[event.user_id] += 1
            # Skip malformed silently, or log if asked
    
    top_users = user_event_counts.most_common(5)

    return {
        "users_by_action": {k: len(v) for k, v in users_by_action.items()},
        "top_users": [{"user": u, "count": c} for u, c in top_users]
    }

# Usage
if __name__ == "__main__":
    result = process_log_file("events.log")
    print(json.dumps(result, indent=2))
