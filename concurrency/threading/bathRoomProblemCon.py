
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

bathRoomCondition = threading.Condition()


def person(i):
    with bathRoomCondition:
        logging.info(f"Person-{i} is waiting to enter bathroom.")
        bathRoomCondition.wait()
        logging.info(f"Person-{i} has entered the bathroom.")
        # time.sleep(2): 
        # yaha daal dia to sari person threads waiting ke liye b block rahengi as 
        # ye thread isss lock ko hold kiye huye hai
        # beech me pause hokar koi thread chal sakti hai but person() vali jaise chalengi
        # vo to lock ki vajah se block ho jaengi 

    time.sleep(2) 
    logging.info(f"Person-{i} is leaving the bathroom.")
    with bathRoomCondition:
        bathRoomCondition.notify()


def bathroom():
    # pass
    with bathRoomCondition:
        bathRoomCondition.notify()


def peopleComing():
    i = 1
    while True:
        t1 = threading.Thread(target=person, args=(i,), daemon=True)
        t1.start()
        time.sleep(random.uniform(0.25, 0.5))
        i += 1


threading.Thread(target=peopleComing, daemon=True).start()
threading.Thread(target=bathroom, daemon=True).start()

time.sleep(25)