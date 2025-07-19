
import random
import time
import threading

roomLock = threading.Lock()
driverCount = 0
riderCount = 0
driverSem = threading.Semaphore(0)
riderSem = threading.Semaphore(0)


def driver(i):
    global driverCount
    global riderCount
    print(f"Driver {i} is in room !")
    with roomLock:
        driverCount = driverCount+1
        if driverCount>=1 and riderCount>=2:
            driverSem.release()
            riderSem.release()
            riderSem.release()
            driverCount -= 1
            riderCount -= 2
    driverSem.acquire()
    print(f"    Driver {i} is ready !!")


def rider(i):
    global driverCount
    global riderCount
    print(f"Rider {i} is in room !")
    with roomLock:
        riderCount = riderCount+1
        if driverCount>=1 and riderCount>=2:
            driverSem.release()
            riderSem.release()
            riderSem.release()
            driverCount -= 1
            riderCount -= 2
    riderSem.acquire()
    print(f"    Rider {i} is ready !!")


def driversComingThread():
    for i in range(5):
        t = threading.Thread(target=driver, args=(i,), daemon=True)
        t.start()
        time.sleep(random.randint(1, 3))


def ridersComingThread():
    for i in range(9):
        t = threading.Thread(target=rider, args=(i,), daemon=True)
        t.start()
        time.sleep(random.randint(2, 4))

t1 = threading.Thread(target=driversComingThread, daemon=True)
t2 = threading.Thread(target=ridersComingThread, daemon=True)

t1.start()
t2.start()

t1.join()
t2.join()
