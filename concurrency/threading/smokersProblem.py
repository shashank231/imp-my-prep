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

onTable = []
ingredients = ["i1", "i2", "i3"]
condition = threading.Condition()
onTableExpect = {
    1: Counter({"i2": 1, "i3": 1}),
    2: Counter({"i1": 1, "i3": 1}),
    3: Counter({"i2": 1, "i1": 1}),
}


def setIngredientsFromAgent():
    global onTable
    while True:
        with condition:
            onTable = [
                ingredients[random.randint(0, 2)],
                ingredients[random.randint(0, 2)],
            ]
            logging.info(f"Agent puts: {onTable}")
            condition.notify_all()  # Wake up all smokers
        time.sleep(2)


def smoker(i):
    global onTable, onTableExpect
    while True:
        smoking = False
        with condition:
            while Counter(onTable) != onTableExpect[i]:
                condition.wait()
            logging.info(f"Smoker{i} ✅ ({onTable})")
            onTable = []  # Clear the table
            condition.notify_all()
            smoking = True
        if smoking:
            time.sleep(2)  # Simulate smoking outside the lock


t1 = threading.Thread(target=setIngredientsFromAgent, daemon=True)
t1.start()

for k in range(1, 4):
    t2 = threading.Thread(target=smoker, args=(k,), daemon=True)
    t2.start()

time.sleep(20)
