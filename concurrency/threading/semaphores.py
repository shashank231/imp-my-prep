import time
import threading

sem1 = threading.Semaphore(5)
threads = []

def worker(i):
    print(" - - - *")
    print(sem1)
    # sem1.release()
    sem1.acquire()
    print(sem1)
    sem1.acquire()
    print(sem1)
    print(" - - -")

    print(f"Thread: {i} started")
    time.sleep(1)
    print(f"Thread: {i} ended")


for i in range(3):
    # threading.Thread(target=worker(i)) -> can't do like this because now the woreker will be called here itself
    t = threading.Thread(target=worker, args=(i,))
    t.start()
    time.sleep(1.5)
