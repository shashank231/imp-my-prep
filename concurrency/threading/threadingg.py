
# threading_guide.py
"""
This file covers important threading concepts in Python with examples:
- Creating threads
- Using Lock for synchronization
- Using Queue for task scheduling
- Daemon vs non-daemon threads
- Thread-safe counter
- Event for signaling
- ThreadPoolExecutor (bonus)
"""

import threading
import time
import queue
from concurrent.futures import ThreadPoolExecutor

# ---------------------------
# 1. Basic Thread Creation
# ---------------------------
def basic_thread_example():
    def worker():
        print(f"[Basic] Worker running in thread {threading.current_thread().name}")
        time.sleep(1)

    t = threading.Thread(target=worker)
    t.start()
    t.join()  # Wait for thread to finish

# ---------------------------
# 2. Lock for Synchronization
# ---------------------------
def lock_example():
    lock = threading.Lock()
    counter = 0

    def increment():
        nonlocal counter
        for _ in range(100000):
            with lock:
                counter += 1

    threads = [threading.Thread(target=increment) for _ in range(5)]
    for t in threads: t.start()
    for t in threads: t.join()

    print(f"[Lock] Final counter value: {counter}")

# ---------------------------
# 3. Using Queue for Thread-safe Task Scheduling
# ---------------------------
def queue_example():
    q = queue.Queue()

    def worker():
        while True:
            try:
                item = q.get(timeout=1)
                print(f"[Queue] Processing {item}")
                time.sleep(0.5)
                q.task_done()
            except queue.Empty:
                break

    for i in range(5):
        q.put(f"task-{i}")

    threads = [threading.Thread(target=worker) for _ in range(2)]
    for t in threads: t.start()
    q.join()
    for t in threads: t.join()

# ---------------------------
# 4. Daemon vs Non-Daemon Threads
# ---------------------------
def daemon_thread_example():
    def background_task():
        while True:
            print("[Daemon] Running background task...")
            time.sleep(1)

    t = threading.Thread(target=background_task, daemon=True)
    t.start()
    time.sleep(3)
    print("[Daemon] Main thread exiting. Background thread will be killed.")

# ---------------------------
# 5. Event for Signaling
# ---------------------------
def event_example():
    event = threading.Event()

    def waiter():
        print("[Event] Waiting for event...")
        event.wait()
        print("[Event] Event triggered!")

    t = threading.Thread(target=waiter)
    t.start()
    time.sleep(2)
    event.set()  # Signal the thread to continue
    t.join()

# ---------------------------
# 6. ThreadPoolExecutor (Bonus: Higher-level API)
# ---------------------------
def thread_pool_example():
    def task(n):
        print(f"[Pool] Running task {n}")
        time.sleep(1)
        return f"Done {n}"

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(task, i) for i in range(5)]
        for f in futures:
            print(f.result())

# ---------------------------
# Run all examples
# ---------------------------
if __name__ == "__main__":
    print("\n--- Basic Thread ---")
    basic_thread_example()

    print("\n--- Lock Example ---")
    lock_example()

    print("\n--- Queue Example ---")
    queue_example()

    print("\n--- Daemon Thread Example ---")
    daemon_thread_example()

    print("\n--- Event Example ---")
    event_example()

    print("\n--- ThreadPoolExecutor Example ---")
    thread_pool_example()
