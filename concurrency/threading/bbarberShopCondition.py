import random
import time
import threading
import logging
from queue import Queue

# Configure logging with timestamps (including milliseconds)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d [%(threadName)s] %(message)s',
    datefmt='%H:%M:%S'
)

capacity = 5
waiting_room = Queue(maxsize=capacity)
barber_ready = threading.Condition()
mutex = threading.Lock()

def barber():
    while True:
        with barber_ready:
            while waiting_room.empty():
                logging.info("Barber is sleeping ...")
                barber_ready.wait()
            customer_id = waiting_room.get()
            logging.info(f"Customer {customer_id} is on the seat ...")
            logging.info(f"Barber is cutting hair of Customer {customer_id} ...")
        time.sleep(2)
        logging.info(f"Haircut done for Customer {customer_id}")

def customer(customer_id):
    with mutex:
        if waiting_room.full():
            logging.info(f"Customer {customer_id} is leaving due to full barber shop.")
            return
        waiting_room.put(customer_id)
        logging.info(f"Customer {customer_id} is waiting ...")

    with barber_ready:
        barber_ready.notify()

# Start the barber thread
barber_thread = threading.Thread(target=barber, daemon=True, name="BarberThread")
barber_thread.start()

# Spawn 10 customers at random intervals
for i in range(10):
    threading.Thread(target=customer, args=(i,), name=f"Customer-{i}").start()
    time.sleep(random.uniform(0.5, 1.5))

# Allow time for all haircuts to complete
time.sleep(20)
