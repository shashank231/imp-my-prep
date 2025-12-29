import time
from collections import deque, defaultdict
from typing import Dict, List, Optional
import statistics


class MetricsStore:
    def __init__(self, max_samples_per_metric: int = 10000):
        self.metrics = defaultdict(lambda: deque(maxlen=max_samples_per_metric))
        self.tags = defaultdict(lambda: defaultdict(list))  # metric -> tag -> timestamps
    
    def record_metric(self, name: str, value: float, tags: Dict[str, str] = None):
        """Record metric with optional tags."""
        timestamp = time.time()
        self.metrics[name].append((timestamp, value))
        
        # Index by tags for filtering
        if tags:
            for tag_key, tag_value in tags.items():
                tag_str = f"{tag_key}:{tag_value}"
                self.tags[name][tag_str].append(timestamp)
    
    def get_metrics(self, name: str, window_seconds: int) -> List[float]:
        """Get all values in time window."""
        now = time.time()
        cutoff = now-window_seconds
        values = []
        for ts, value in self.metrics[name]:
            if ts >= cutoff:
                values.append(value)
        return values

    def get_percentile(self, name: str, p: float, window_seconds: int) -> Optional[float]:
        """P95, P99 etc. in time window."""
        values = self.get_metrics(name, window_seconds)
        if not values:
            return None
        
        return round(statistics.quantiles(values, n=100)[int(p * 100)], 2)
    
    def get_metrics_by_tag(self, name: str, tag_key: str, tag_value: str, 
                          window_seconds: int) -> List[float]:
        """Filter by tag (bonus)."""
        now = time.time()
        cutoff = now - window_seconds
        
        tag_str = f"{tag_key}:{tag_value}"
        relevant_timestamps = self.tags[name][tag_str]
        
        values = []
        for ts, value in self.metrics[name]:
            if (ts >= cutoff and 
                ts in relevant_timestamps):  # Approximate tag filter
                values.append(value)
        
        return values

# Usage / Test
if __name__ == "__main__":
    metrics = MetricsStore()
    
    # Simulate query latencies
    metrics.record_metric("query_latency_ms", 25.3, {"dataset": "users"})
    metrics.record_metric("query_latency_ms", 150.7, {"dataset": "orders"})
    metrics.record_metric("query_latency_ms", 89.2, {"dataset": "users"})
    metrics.record_metric("query_latency_ms", 200.1, {"dataset": "users"})
    metrics.record_metric("query_latency_ms", 45.6, {"dataset": "orders"})
    
    # P95 last 300s
    p95 = metrics.get_percentile("query_latency_ms", 0.95, 300)
    print(f"P95: {p95}")  # ~175ms
    
    # Users only
    users_only = metrics.get_metrics_by_tag("query_latency_ms", "dataset", "users", 300)
    print(f"Users P95: {metrics.get_percentile_for_list(users_only, 0.95)}")
