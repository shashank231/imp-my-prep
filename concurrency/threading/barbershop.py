import time
import random
import threading

n = 0
capacity = 3
lock1 = threading.Lock()
bar_sem = threading.Semaphore(0)
customer_sem = threading.Semaphore(0)

def barber():
    global n
    while True:
        with lock1:
            if n>0:
                print("Barber cutting !!")
                time.sleep(1)
                customer_sem.release()
                n = n-1
        if n==0:
            print("Barber sleeping !!")
            bar_sem.acquire()


def customer(i):
    global n
    global capacity
    with lock1:
        if n >= capacity:
            print(f"Customer-{i} leaving: shop full")
            return
        n += 1
        print(f"Customer-{i} entered shop. Waiting: {n}")
    bar_sem.release()
    customer_sem.acquire()
    print(f"Customer-{i} got haircut!")


# Start barber thread
barber_thread = threading.Thread(target=barber, daemon=True)
barber_thread.start()

# Simulate 10 customers arriving at random intervals
for i in range(10):
    threading.Thread(target=customer, args=(i,)).start()
    time.sleep(random.uniform(0.2, 0.5))

# Give enough time for all haircuts to finish
time.sleep(10)