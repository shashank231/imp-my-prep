import random
import time
import threading
import logging
from collections import Counter

# Configure logging with timestamps (including milliseconds)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d [%(threadName)s] %(message)s',
    datefmt='%H:%M:%S'
)

condition = threading.Condition()


def foo():
    with condition:
        while True:
            print("foo")
            condition.notify_all()
            condition.wait()
            time.sleep(1)


def bar():
    with condition:
        while True:
            print("bar")
            condition.notify_all()
            condition.wait()
            time.sleep(1)



t1 = threading.Thread(target=foo)
t2 = threading.Thread(target=bar)

t1.start()
t2.start()

