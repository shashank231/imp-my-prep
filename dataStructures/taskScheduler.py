import time
import threading
import queue
from typing import Callable


class TaskScheduler:

    def __init__(self, num_workers: int):
        self.num_workers = num_workers
        self.task_queue = None
        self.threads = []
        self.shutdown_flag = threading.Event()

    def set_queue(self):
        self.task_queue = queue.Queue()

    def add_to_queue(self, task: Callable):
        if not self.task_queue:
            raise ValueError("Queue not initialized. Call set_queue() first.")
        self.task_queue.put(task)

    def start(self):
        if not self.task_queue:
            raise ValueError("Queue not initialized. Call set_queue() first.")

        def worker():
            while not self.shutdown_flag.is_set():
                try:
                    task = self.task_queue.get(timeout=1)
                    task()
                    self.task_queue.task_done()
                except queue.Empty:
                    continue

        for _ in range(self.num_workers):
            t = threading.Thread(target=worker)
            t.daemon = True
            t.start()
            self.threads.append(t)

    def wait_for_all(self):
        if self.task_queue:
            self.task_queue.join()

    def run(self):
        for t in self.threads:
            t.join()

    def end(self):
        self.shutdown_flag.set()
        for t in self.threads:
            t.join()


# Example usage:
def example_task(i):
    print(f"Task {i} started")
    time.sleep(1)
    print(f"Task {i} finished")

scheduler = TaskScheduler(num_workers=3)
scheduler.set_queue()
scheduler.start()

# def make_task(i):
#     def task():
#         example_task(i)
#     return task

# for i in range(5):
#     scheduler.add_to_queue(make_task(i))

# for i in range(5):
#     scheduler.add_to_queue(lambda i=i: example_task(i))

from functools import partial

for i in range(5):
    task = partial(example_task, i)
    scheduler.add_to_queue(task)


scheduler.wait_for_all()
scheduler.run()
scheduler.end()
