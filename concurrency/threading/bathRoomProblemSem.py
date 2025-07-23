
import time
import random
import threading
import logging
from collections import Counter

# Configure logging with timestamps (including milliseconds)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d [%(threadName)s] %(message)s',
    datefmt='%H:%M:%S'
)

bathroomLock = threading.Semaphore(1)

def person(i):
    logging.info(f"Person-{i} is waiting to enter bathroom.")
    bathroomLock.acquire()
    logging.info(f"Person-{i} has entered the bathroom.")
    time.sleep(2)
    logging.info(f"Person-{i} is leaving the bathroom.")
    bathroomLock.release()


def peopleComing():
    i = 1
    while True:
        t1 = threading.Thread(target=person, args=(i,), daemon=True)
        t1.start()
        time.sleep(random.uniform(0.25, 0.5))
        i += 1


threading.Thread(target=peopleComing, daemon=True).start()
time.sleep(25)

