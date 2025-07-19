
# Use collections.deque for most queue use-cases (FIFO, LIFO) — it’s fast and memory-efficient.
# Use queue.Queue only in multi-threaded programs (thread-safe).
# Avoid lists for queue-like operations because they’re inefficient (O(n) pops from the front).

# ✅ Time Complexity:
    # append(): O(1)
    # appendleft(): O(1)
    # pop(): O(1)
    # popleft(): O(1)

# Why Use deque?
    # Implemented as a doubly-linked list, optimized for fast append/pop from both ends.
    #                 ---------------------
    # Thread-safe for simple use cases (no need for full locks).
    # Best suited for FIFO, LIFO, and sliding window problems.

# queue.Queue — For Thread-Safe Queues
    # ✅ Use-case: In multi-threaded programs, where you need safe communication between producer and consumer threads.
    # ⛔ Drawback: Slightly slower than deque due to locking overhead.
from queue import Queue
q = Queue()
q.put(1)        # enqueue
q.get()         # dequeue


# list — ❌ Not Recommended for Queues
    # Why You Should Avoid:
        # Popping from the beginning is slow for large lists.
        # Not designed for queue-like use.
        # 🚫 Time Complexity:
            # append(): O(1)
            # pop(0): O(n) (because all elements shift after popping front)
q = []
q.append(1)     # enqueue
q.pop(0)        # dequeue (bad!)


# 🧠 Pro Tip
# For bounded queues, use:
from collections import deque
q = deque(maxlen=100)
