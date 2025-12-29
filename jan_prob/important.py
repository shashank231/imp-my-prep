import os
import uuid
from enum import Enum
from dataclasses import dataclass
@dataclass
class LogEvent:
    timestamp: str
    user_id: str
    action: str
    status: str
line = "2025-12-24T18:42:05Z|user123|purchase|success"
parts = line.strip().split('|')
LogEvent(*parts)



# from pathlib import Path
# if not Path(filepath).exists():
#     raise FileNotFoundError(f"File {filepath} not found")
# with open(filepath, 'r') as f:
#     for line_num, line in enumerate(f, 1):
#         event = parse_line(line)



from collections import Counter
# You can initialize a Counter by passing it an iterable (like a list or string), a dictionary, or keyword arguments.
# From a list
c = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
# Result: Counter({'apple': 3, 'banana': 2, 'orange': 1})
# From a string
c.most_common(2)  # returns [Tuple(ele, count)...]
s = Counter("mississippi")
# Result: Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
c1 = Counter()
print(c1["a"])  # 0
print(c1["b"])  # 0
c1["a"] += 1
c1["a"] += 1
print(c1["a"])  # 2
print(c1["b"])  # 0








# Multiprocessing example
import os
from multiprocessing import Pool
num_workers = os.cpu_count()

def task(num):
    return (num, num * num)

numbs = [1, 2, 3, 4, 5]
with Pool(num_workers) as pool:
    partial_results = pool.map(task, numbs)
for result in partial_results:
    print(result)





# Sliding Log Rate Limiter example
from threading import Lock
from time import time
now = time()
dict_of_dequeue_of_timestamps_for_each_user = {}
window_seconds = 60
max_requests = 5

def _():
    with Lock():
        # Remove expired requests
        user_requests = dict_of_dequeue_of_timestamps_for_each_user.get("user_id", [])
        cutoff = now - window_seconds
        while user_requests and user_requests[0] <= cutoff:
            user_requests.popleft()

        # Check limit
        if len(user_requests) < max_requests:
            user_requests.append(now)
            return True, max_requests - len(user_requests)
        
        return False, 0



# Enum example
class Status(Enum):
    TO_DO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"
for i in Status:
    print(f"{i.name}, {i.value}")
s1 = Status("todo").name    # TO_DO (str type)
s2 = Status("wrong_value")  # Raises ValueError



# UUID example
task_id = str(uuid.uuid4())



# Sorting dictionary by values example
dict1 = dict(a=2, b=4, c=1, d=3)
d1 = sorted(
    dict1.items(),      # returns list of tuples [(key, value), ...]
    key=lambda x: x[1], # sort by value
    reverse=True        # descending order
)
print(d1)





import heapq
arr = [(1, "ab"), (2, "cd")]
heapq.heapify(arr)              # Min-heap in-place
heapq.heappush(arr, (3, "ef"))  # Insert 
peek_min = arr[0]              # Peek at the smallest element
print("Peek:", peek_min)       # Output: (1, "ab")
min_elem = heapq.heappop(arr)  # Remove the smallest element
print("Popped:", min_elem)     # Output: (1, ab)
print("Heap Now:", arr)        # Output: [(2, cd), (3, ef)]

# remove a paticular element
heap = [10, 20, 15, 30, 40]
heapq.heapify(heap)
# 1. Remove the value
heap.remove(15) 
# 2. Re-heapify to fix the structure
heapq.heapify(heap) 

