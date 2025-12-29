import json
from dataclasses import dataclass
from collections import defaultdict, Counter
from pathlib import Path
from typing import Dict, List, Any, Optional
import statistics
from datetime import datetime




@dataclass
class Event:
    timestamp: float      # Unix timestamp
    user_id: str
    event_type: str
    duration_ms: float





class JSONLProcessor:
    def __init__(self):
        self.events_by_type: Dict[str, List[float]] = defaultdict(list)
        self.user_counts = Counter()
        self.error_count = 0
        self.total_events = 0
        self.total_lines = 0  # SINGLE COUNTER: ALL window lines attempted
    
    def _unix_timestamp(self, iso_str: str) -> Optional[float]:
        """ISO → Unix timestamp."""
        try:
            dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
            return int(dt.timestamp())
        except (ValueError, KeyError):
            return None
    
    def _parse_line(self, line: str, line_num: int) -> Optional[Event]:
        """Full JSONL parse → Event."""
        try:
            data = json.loads(line.strip())
            ts = self._unix_timestamp(data["timestamp"])
            if ts is None:
                return None
            
            duration = data.get("duration_ms")
            if duration is None:
                return None
            
            return Event(ts, data["user_id"], data["event_type"], float(duration))
        except (json.JSONDecodeError, KeyError, ValueError):
            return None



    def process_file(self, filepath: str, start_time: str, end_time: str) -> Dict[str, Any]:
        """Window-scoped processing."""
        filepath = Path(filepath)
        if not filepath.exists():
            raise FileNotFoundError(f"{filepath} not found")
        
        start_ts = self._unix_timestamp(start_time)
        end_ts = self._unix_timestamp(end_time)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                # 1. Quick timestamp check FIRST
                try:
                    data = json.loads(line.strip())
                    ts = self._unix_timestamp(data.get("timestamp"))
                    
                    # 2. OUTSIDE window? Skip completely
                    if ts is None or not (start_ts <= ts <= end_ts):
                        continue
                    
                    # 3. INSIDE WINDOW: SINGLE COUNTER
                    self.total_lines += 1  # ALL lines attempted in window
                    
                    # 4. Full validation
                    event = self._parse_line(line, line_num)
                    if event is None:
                        self.error_count += 1  # Failed parse
                    else:
                        self._aggregate_event(event)
                        self.total_events += 1  # Success!
                        
                except json.JSONDecodeError:
                    # Malformed JSON inside window
                    self.total_lines += 1
                    self.error_count += 1
                    continue
        
        return self._generate_report(start_time, end_time)



    def _aggregate_event(self, event: Event):
        """Update aggregates."""
        self.events_by_type[event.event_type].append(event.duration_ms)
        self.user_counts[event.user_id] += 1
    
    def _generate_report(self, start_time: str, end_time: str) -> Dict[str, Any]:
        """Window-scoped metrics."""
        p95_by_event = {}
        for event_type, durations in self.events_by_type.items():
            if durations:
                p95_by_event[event_type] = round(
                    statistics.quantiles(durations, n=100)[95], 2
                )
        
        top_users = self.user_counts.most_common(3)
        success_rate = (
            round(self.total_events / self.total_lines * 100, 1)
            if self.total_lines > 0 else 0
        )
        
        return {
            "p95_by_event": p95_by_event,
            "top_users": [{"user": u, "count": c} for u, c in top_users],
            "error_count": self.error_count,      # Failed parses in window
            "total_events": self.total_events,    # Successful events in window
            "total_lines": self.total_lines,      # ALL lines attempted in window
            "success_rate": success_rate,         # Perfect math!
            "time_window": f"{start_time} to {end_time}"
        }





# Test
if __name__ == "__main__":
    TEST_DATA = """{"timestamp": "2025-12-24T18:38:00Z", "user_id": "alice", "event_type": "login", "duration_ms": 25}
{"timestamp": "2025-12-24T18:39:15Z", "user_id": "bob", "event_type": "purchase", "duration_ms": 150}
{"timestamp": "2025-12-24T18:40:22Z", "user_id": "alice", "event_type": "logout", "duration_ms": 12}
{"timestamp": "2025-12-24T18:41:10Z", "user_id": "charlie", "event_type": "error"}
{"timestamp": "2025-12-24T18:42:05Z", "malformed": "json"}"""
    
    with open("events.jsonl", "w") as f:
        f.write(TEST_DATA)
    
    processor = JSONLProcessor()
    result = processor.process_file(
        "events.jsonl",
        "2025-12-24T18:40:00Z",
        "2025-12-24T18:45:00Z"
    )
    print(json.dumps(result, indent=2))
