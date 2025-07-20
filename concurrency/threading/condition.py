

import threading
import time

start_event = threading.Event()

def worker():
    print("Waiting to start...")
    start_event.wait()
    print("Started working!")

def worker2():
    print("Waiting to start...")
    start_event.wait()
    print("Started working!")

def worker3():
    print("Waiting to start...")
    start_event.wait()
    print("Started working!")

threading.Thread(target=worker).start()
threading.Thread(target=worker2).start()
threading.Thread(target=worker3).start()

time.sleep(1)
start_event.set()
