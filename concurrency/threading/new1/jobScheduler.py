import threading
import time
import heapq
from dataclasses import dataclass, field
from typing import Callable


# --------------------------------------
# Job Representation
# --------------------------------------
@dataclass(order=True)
class Job:
    priority: int
    run_at: float
    job_id: int = field(compare=False)
    task: Callable = field(compare=False)
    cancelled: bool = field(default=False, compare=False)

    def run(self):
        if not self.cancelled:
            print(f"[{time.strftime('%X')}] Running job {self.job_id}")
            try:
                self.task()
            except Exception as e:
                print(f"[{time.strftime('%X')}] Error in job {self.job_id}: {e}")
        else:
            print(f"[{time.strftime('%X')}] Job {self.job_id} was cancelled")


# --------------------------------------
# Job Scheduler Class
# --------------------------------------
class JobScheduler:
    def __init__(self, worker_count=4):
        self.job_queue = []
        self.lock = threading.Lock()
        self.cv = threading.Condition(self.lock)
        self.job_id_counter = 0
        self.running = True

        # Start worker threads
        self.threads = [
            threading.Thread(target=self.worker, daemon=True)
            for _ in range(worker_count)
        ]
        for t in self.threads:
            t.start()

    # Schedule a job with optional delay and priority
    def schedule(self, task: Callable, delay: float = 0, priority: int = 10) -> int:
        with self.lock:
            self.job_id_counter += 1
            run_at = time.time() + delay
            job = Job(priority=priority, run_at=run_at, job_id=self.job_id_counter, task=task)
            heapq.heappush(self.job_queue, job)
            self.cv.notify()
            return job.job_id

    # Cancel a job by ID
    def cancel(self, job_id: int):
        with self.lock:
            for job in self.job_queue:
                if job.job_id == job_id:
                    job.cancelled = True
                    print(f"[{time.strftime('%X')}] Cancelled job {job_id}")
                    break

    # Worker thread logic
    def worker(self):
        while self.running:
            with self.cv:
                while not self.job_queue:
                    self.cv.wait()

                job = self.job_queue[0]
                now = time.time()

                if job.run_at > now:
                    timeout = job.run_at - now
                    self.cv.wait(timeout=timeout)
                    continue

                heapq.heappop(self.job_queue)

            # Run the job outside the lock
            job.run()

    # Graceful shutdown
    def shutdown(self):
        self.running = False
        with self.cv:
            self.cv.notify_all()
        for t in self.threads:
            t.join()


# --------------------------------------
# Example usage
# --------------------------------------
if __name__ == "__main__":
    scheduler = JobScheduler(worker_count=3)

    def job_func(msg):
        def inner():
            print(f"[{time.strftime('%X')}] Job says: {msg}")
        return inner

    # Schedule jobs with different delays and priorities
    job1 = scheduler.schedule(job_func("Low priority"), delay=2, priority=10)
    job2 = scheduler.schedule(job_func("High priority"), delay=1, priority=1)
    job3 = scheduler.schedule(job_func("Medium priority"), delay=1.5, priority=5)

    # Cancel job 3 before it executes
    time.sleep(1.2)
    scheduler.cancel(job3)

    # Let jobs finish
    time.sleep(5)
    scheduler.shutdown()
