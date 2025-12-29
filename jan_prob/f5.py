# {"timestamp": "2025-12-24T18:38:00Z", "user_id": "alice", "event": "login", "duration_ms": 25}
# {"timestamp": "2025-12-24T18:39:15Z", "user_id": "bob", "event": "purchase", "duration_ms": 150}
# {"timestamp": "2025-12-24T18:40:22Z", "user_id": "alice", "event": "logout", "duration_ms": 12}
# {"timestamp": "2025-12-24T18:41:10Z", "user_id": "charlie", "event": "error", "duration_ms": null}
# {"timestamp": "2025-12-24T18:42:05Z", "malformed": "json"}  ← BAD LINE

# {
#   "p95_by_event": {"login": 25.0, "purchase": 150.0},
#   "top_users": [{"user": "alice", "count": 2}, {"user": "bob", "count": 1}],
#   "error_count": 2,
#   "total_events": 3,
#   "time_window": "2025-12-24T18:40:00Z to 18:45:00Z"
# }


import numpy as np
p95 = np.percentile(latencies, 95)
from pathlib import Path
from collections import defaultdict, Counter
from dataclasses import dataclass


@dataclass
class LogLine:
    timestamp: str
    user_id: str
    event: str
    duration: str


class JSONLProcessor:

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.total_events = 0
        self.error_count = 0
        self.users = Counter()
        self.storage = defaultdict(list)

    def _validate_file_path(self) -> Path:
        path = Path(self.file_path)
        if not path.exists():
            raise ValueError(f"File does not exist: {self.file_path}")
        if not path.is_file():
            raise ValueError(f"Path is not a file: {self.file_path}")
        return path

    def _parse_line(self, line: str):
        stripped_line = line.strip()
        line_entries = stripped_line.split(",")
        if len(line_entries) != 4:
            self.error_count += 1
            return None
        else:
            timestamp, user_id, event, duration = line_entries
            return LogLine(timestamp, user_id, event, duration)

    def _process_full_file(self):
        with open(self.file_path, "r") as f:
            for line_num, line in enumerate(f, 1):
                self.total_events += 1
                logline = self._parse_line(line)
                if not logline:
                    continue
                self.users[logline.user_id] += 1
                self.storage[logline.event].append(
                    (logline.timestamp, logline.duration)
                )

    def process_file(self):
        self._validate_file_path()
        self._process_full_file()

    def calc_stats(self, start_time, end_time):
        p95_by_event
        for 


    def get_stats(self, start_time, end_time):



