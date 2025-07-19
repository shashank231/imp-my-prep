import threading
import time
import random

count = 0
lk = threading.Lock()

def worker():
    global count
    for _ in range(100):
        with lk:
            tmp = count        # read
            time.sleep(0)      # force thread switch
            tmp += 1           # add
            count = tmp        # write
        # tmp = count        # read
        # time.sleep(0)      # force thread switch
        # tmp += 1           # add
        # count = tmp        # write

threads = []

for _ in range(10):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final count:", count)
