import threading
import time
import random

class UberRide:
    def __init__(self):
        self.rider_count = 0
        self.driver_count = 0
        self.lock = threading.Lock()
        self.rider_sem = threading.Semaphore(0)
        self.driver_sem = threading.Semaphore(0)
        self.barrier = threading.Barrier(3)  # 2 riders + 1 driver
        self.ride_id = 1
        self.ride_lock = threading.Lock()

    def rider(self, i):
        print(f"Rider {i} arrived.")
        with self.lock:
            self.rider_count += 1
            if self.rider_count >= 2 and self.driver_count >= 1:
                # We can form a ride
                self.rider_sem.release()
                self.rider_sem.release()
                self.driver_sem.release()
                self.rider_count -= 2
                self.driver_count -= 1
        self.rider_sem.acquire()
        self.board("Rider", i)

    def driver(self, i):
        print(f"Driver {i} arrived.")
        with self.lock:
            self.driver_count += 1
            if self.rider_count >= 2 and self.driver_count >= 1:
                self.rider_sem.release()
                self.rider_sem.release()
                self.driver_sem.release()
                self.rider_count -= 2
                self.driver_count -= 1
        self.driver_sem.acquire()
        self.board("Driver", i)

    def board(self, who, i):
        print(f"    {who} {i} boarding...")
        is_leader = self.barrier.wait() == 0
        if is_leader:
            with self.ride_lock:
                print(f"✅ Ride {self.ride_id} is ready in {who}-{i}!\n")
                self.ride_id += 1
    
    # def board(self, who, i):
    #     print(f"    {who} {i} boarding...")
    #     self.barrier.wait()
    #     with self.ride_lock:
    #         print(f"✅ Ride {self.ride_id} is ready!\n")
    #         self.ride_id += 1




# Driver and Rider arrival simulation
uber = UberRide()

def spawn_riders():
    for i in range(9):
        t = threading.Thread(target=uber.rider, args=(i,))
        t.start()
        time.sleep(random.uniform(0.1, 0.3))

def spawn_drivers():
    for i in range(5):
        t = threading.Thread(target=uber.driver, args=(i,))
        t.start()
        time.sleep(random.uniform(0.2, 0.4))

t1 = threading.Thread(target=spawn_riders)
t2 = threading.Thread(target=spawn_drivers)

t1.start()
t2.start()

t1.join()
t2.join()
