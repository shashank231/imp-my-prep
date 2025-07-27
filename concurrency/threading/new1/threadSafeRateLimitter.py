import time
import random
import threading
import logging
from collections import Counter
from queue import deque

# Configure logging with timestamps (including milliseconds)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d [%(threadName)s] %(message)s',
    datefmt='%H:%M:%S'
)


class RateLimiter:
    def __init__(self, max_requests: int, time_window: float):
        self.max_requests = max_requests
        self.time_window = time_window
        self.timestamps = deque()
        self.lock = threading.Lock()

    def allow(self) -> bool:
        now = time.time()
        with self.lock:
            # Remove outdated timestamps
            while self.timestamps and now - self.timestamps[0] > self.time_window:
                self.timestamps.popleft()

            if len(self.timestamps) < self.max_requests:
                self.timestamps.append(now)
                return True
            else:
                return False
