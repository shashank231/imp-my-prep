import time
import random
import threading
import logging
from queue import Queue

# Configure logging with timestamps (including milliseconds)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d [%(threadName)s] %(message)s',
    datefmt='%H:%M:%S'
)

# Number of philosophers
N = 5

# Locks for each spoon
spoons = [threading.Lock() for _ in range(N)]

# Queue to manage philosopher eating order for fairness
eating_queue = Queue()

# Track eating counts to monitor fairness
eating_counts = [0] * N


def philosopher(i):
    global eating_counts
    # Resource hierarchy: always pick lower-numbered spoon first
    left_spoon = i - 1
    right_spoon = i % N  # Circular table: philosopher 5's right spoon is 1
    spoon1, spoon2 = min(left_spoon, right_spoon), max(left_spoon, right_spoon)

    while True:
        # Request to eat by adding to the queue
        eating_queue.put(i)
        logging.info(f"Philosopher {i} is thinking and waiting to eat")

        # Wait until this philosopher is at the front of the queue
        while eating_queue.queue[0] != i:
            time.sleep(0.1)  # Avoid busy waiting

        # Try to acquire both spoons
        with spoons[spoon1]:
            with spoons[spoon2]:
                # Remove from queue since philosopher can eat
                eating_queue.get()
                eating_counts[i - 1] += 1
                logging.info(f"Philosopher {i} picked up spoons {spoon1 + 1} and {spoon2 + 1}")
                logging.info(f"Philosopher {i} is eating (meal #{eating_counts[i - 1]})")
                time.sleep(random.uniform(1, 3))  # Simulate eating
                logging.info(f"Philosopher {i} finished eating")

        logging.info(f"Philosopher {i} is thinking")
        time.sleep(random.uniform(1, 3))  # Simulate thinking

# Create and start philosopher threads
threads = []
for i in range(1, N + 1):
    t = threading.Thread(target=philosopher, args=(i,), name=f"Philosopher-{i}")
    t.daemon = True
    t.start()

# Run for a fixed duration and print eating counts
time.sleep(40)
logging.info(f"Eating counts: {eating_counts}")