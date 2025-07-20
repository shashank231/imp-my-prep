import time
import threading


class ReadWriteLock:
    def __init__(self):
        self.num_active_readers = 0                  # Count of currently active readers
        self.writer_is_active = False                # True if a writer is currently writing
        self.lock = threading.Lock()                 # Lock to protect access to shared state
        self.condition = threading.Condition(self.lock)  # Condition to wait/notify threads

    def acquire_read(self):
        with self.condition:
            while self.writer_is_active:
                self.condition.wait()                # Wait until no writer is writing
            self.num_active_readers += 1             # Register this reader

    def release_read(self):
        with self.condition:
            self.num_active_readers -= 1             # Reader is done
            if self.num_active_readers == 0:
                self.condition.notify_all()          # Notify potential waiting writers

    def acquire_write(self):
        with self.condition:
            while self.num_active_readers > 0 or self.writer_is_active:
                self.condition.wait()                # Wait until no readers or writers
            self.writer_is_active = True             # Mark writer as active

    def release_write(self):
        with self.condition:
            self.writer_is_active = False            # Mark writer as done
            self.condition.notify_all()              # Notify all waiting readers/writers


# Shared lock for all readers and writers
rw_lock = ReadWriteLock()


def reader(reader_id):
    while True:
        rw_lock.acquire_read()
        print(f"[Reader-{reader_id}] Reading data...")
        time.sleep(1)
        print(f"[Reader-{reader_id}] Finished reading.")
        rw_lock.release_read()
        time.sleep(1)  # Simulate idle time


def writer(writer_id):
    while True:
        rw_lock.acquire_write()
        print(f"[Writer-{writer_id}] Writing data...")
        time.sleep(2)
        print(f"[Writer-{writer_id}] Finished writing.")
 