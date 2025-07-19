import time
import random
import threading

# Semaphores to block threads until a full group is ready
rider_sem = threading.Semaphore(0)
driver_sem = threading.Semaphore(0)

# Shared counters
rider_count = 0
driver_count = 0
# Lock for safely updating shared counters
lock = threading.Lock()
# Barrier for starting the ride together (3 threads)
ride_barrier = threading.Barrier(3)

 
def rider():
    global rider_count, driver_count
    with lock:
        rider_count += 1
        if rider_count >= 2 and driver_count >= 1:
            # Form a group
            rider_count -= 2
            driver_count -= 1
            rider_sem.release()
            rider_sem.release()
            driver_sem.release()
        else:
            # Wait to be released
            pass
    rider_sem.acquire()
    ride_barrier.wait()
    print(f"🚗 Rider riding with a driver")

def driver():
    global rider_count, driver_count
    with lock:
        driver_count += 1
        if rider_count >= 2 and driver_count >= 1:
            # Form a group
            rider_count -= 2
            driver_count -= 1
            rider_sem.release()
            rider_sem.release()
            driver_sem.release()
        else:
            # Wait to be released
            pass
    driver_sem.acquire()
    ride_barrier.wait()
    print(f"🚕 Driver driving riders")

# Test function to spawn threads
def test_uber_ride():
    threads = []
    for _ in range(6):  # 6 riders
        t = threading.Thread(target=rider)
        threads.append(t)
        t.start()
        time.sleep(random.uniform(0.1, 0.3))

    for _ in range(3):  # 3 drivers
        t = threading.Thread(target=driver)
        threads.append(t)
        t.start()
        time.sleep(random.uniform(0.1, 0.3))

    for t in threads:
        t.join()

if __name__ == "__main__":
    test_uber_ride()
