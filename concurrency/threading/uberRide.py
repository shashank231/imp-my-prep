import threading

class Uber:
    def __init__(self):
        self.rider_count = 0
        self.driver_count = 0
        self.lock = threading.Lock()

        self.rider_sem = threading.Semaphore(0)
        self.driver_sem = threading.Semaphore(0)

        self.group_lock = threading.Lock()
        self.board_count = 0

    def rider(self, boardRider):
        with self.lock:
            self.rider_count += 1
            if self.rider_count >= 2 and self.driver_count >= 1:
                self.rider_sem.release()
                self.rider_sem.release()
                self.driver_sem.release()
                self.rider_count -= 2
                self.driver_count -= 1

        self.rider_sem.acquire()
        self.board(boardRider)

    def driver(self, boardDriver):
        with self.lock:
            self.driver_count += 1
            if self.rider_count >= 2 and self.driver_count >= 1:
                self.rider_sem.release()
                self.rider_sem.release()
                self.driver_sem.release()
                self.rider_count -= 2
                self.driver_count -= 1

        self.driver_sem.acquire()
        self.board(boardDriver)

    def board(self, action):
        with self.group_lock:
            action()
            self.board_count += 1
            if self.board_count == 3:
                print(" | ride complete")
                self.board_count = 0


def boardRider():
    print("R", end='')

def boardDriver():
    print("D", end='')

uber = Uber()
threads = []

# Simulate 6 riders, 3 drivers = 3 rides
for _ in range(6):
    threads.append(threading.Thread(target=uber.rider, args=(boardRider,)))

for _ in range(2):
    threads.append(threading.Thread(target=uber.driver, args=(boardDriver,)))

# Shuffle to simulate random arrival
import random
random.shuffle(threads)

# Start all threads
for t in threads:
    t.start()
for t in threads:
    t.join()
