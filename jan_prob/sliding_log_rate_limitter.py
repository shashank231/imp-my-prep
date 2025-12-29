from collections import defaultdict, deque
from time import time
from threading import Lock
from typing import Optional, Dict, Any, Tuple

# This is Sliding Window Log—deque stores exact timestamps, cleanup old ones. 
# Precise but memory-bound. Token Bucket would refill predictably but allow bursts. 
# Redis? Sorted Set for distributed sliding window.

class RateLimiter:

    def __init__(self, max_requests: int = 5, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(deque)  # user_id -> deque of timestamps
        self.lock = Lock()  # Thread-safe
    
    def is_allowed(self, user_id: str) -> bool:
        """Check if user can make request. Returns (allowed: bool, remaining: int)."""
        now = time()
        
        with self.lock:
            # Remove expired requests
            user_requests = self.requests[user_id]
            cutoff = now - self.window_seconds
            while user_requests and user_requests[0] <= cutoff:
                user_requests.popleft()
            
            # Check limit
            if len(user_requests) < self.max_requests:
                user_requests.append(now)
                return True, self.max_requests - len(user_requests)
            
            return False, 0
    
    def get_stats(self, user_id: str) -> Dict[str, Any]:
        """Bonus: user stats."""
        with self.lock:
            reqs = self.requests[user_id]
            return {
                "count": len(reqs),
                "remaining": self.max_requests - len(reqs),
                "reset_in": max(0, self.window_seconds - (time() - reqs[0]))
            }

# Usage / Test
if __name__ == "__main__":
    limiter = RateLimiter(max_requests=3, window_seconds=10)
    
    for i in range(5):
        allowed, remaining = limiter.is_allowed("user123")
        print(f"Request {i+1}: {allowed}, remaining: {remaining}")
    
    print(limiter.get_stats("user123"))
