
# threading.Thread(target=worker, args=(i,), daemon=True)
# threading.Lock()
# ---------------
# Important thing to understand here is, difference between pausing and  blocking
# When a thread is holding a lock,
    # it can also pass control to some other thread, lets say inside a lock you called 
    # event.wait(), now the control goes to thread 2, but then thread1 will be blocked untill that event 
    # is set, and if some other thread is using same lock, that thread won't be able to acquire 
    # lock as that lock is already acquired by thread1
    # and thread1 will kept being locked only control will go to some other thread


# semaphore
# ---------
# sem1 = threading.Semaphore(count)
# sem1.acquire()
    # semaphore are already thread safe
    # can be called with and without lock(preferred)
    # if called inside lock: thread will hold the lock while waiting 
# sem1.release()

# condition
# ----------
# con1 = threading.condition(lock)
# con1.wait()
    # should be called inside with condition: (has internal lock)
    # if called inside lock: thread will release the lock while waiting 
    # Always use condn.wait() inside a while loop (due to spurious wakeups) or we can also use condn.wait_for()
        # with condn:
        #     while not ready:
        #         condn.wait()
        # with condn:
        #     condn.wait_for(lambda: ready)
        # ---------------------------------
        # with condn:
        #     while conter<5:
        #         condn.wait()
        # with condn:
        #     condn.wait_for(lambda: counter>=5)

# con1.notify()
    # should be called inside with condition: (has internal lock)
    # called inside lock(condition): thread will release the lock while waiting 

# b1 = threading.Barrier(num_of_threads)
# is_leader = b1.wait() == False


# Threads 
# Memory Model
# Memory Type	                  Shared Across Threads?	Notes
# Global Variables	              ✅ Yes      	           Must protect with locks if writing
# Heap Objects	                  ✅ Yes                    Shared unless isolated per thread
# Function Locals	              ❌ No	                   Each thread has its own stack (its own local vars)
# # Thread-local Storage	      ❌ No (by design)         Can be implemented using threading.local()


# IMMUTABLE
# ---------
# Even immutable data types like int, str, etc., aren't safe when you're doing operations like x += 1 because they involve:
# Read → Modify → Write
# # Which is not atomic, and threads can interleave during this.
# Thread A:
# LOAD x → reads 10
# interrupted before increment

# Thread B:
# LOAD x → also reads 10
# INCREMENT → gets 11
# STORE x → writes back 11

# Back to Thread A:
# INCREMENT → adds 1 to its old 10 → gets 11
# STORE x → writes back 11
# ❌ Final value of x = 11 — but it should be 12!
# Both threads thought they incremented, but one of them overwrote the other’s work.


# MUTABLE
# ---------
# Mutable data (like dict, list, set) can be even more dangerous:
# One thread might iterate, and control goes to another which will modify the same object which previous one was reading..
# You can get RuntimeError, corrupted states, or worse — silent bugs.

# 🔐 What a Thread Lock Actually Does (in Python)
# A thread lock (like threading.Lock) does not prevent the OS from context switching between threads.
# ❗ Instead, it prevents multiple threads from entering a critical section at the same time.

# ✅ Correct understanding:
# When one thread acquires a lock, other threads trying to acquire the same lock will block (i.e., they'll wait).
# This ensures that only one thread at a time can enter the protected section (the critical section).

# ❌ Common Misconception:
# "Lock stops OS from switching threads while one is running" ***VI***
# This is not true — the OS can still switch context (i.e., pause this thread and schedule another), even if the thread is inside a with lock: block.
# But:
# The lock stays acquired by the original thread, so no other thread can enter the critical section until the original thread releases the lock.
# Even if another thread starts running, when it tries to lock.acquire(), it will block and wait.

#  So how do you really benefit from immutability?
# ------------------------------------------------
# You do this:
    # Keep shared immutable data as read-only (never rebind it globally).
    # If a thread needs a modified version, it creates its own local copy.
        # def thread_fn():
        #    local_value = shared_value + 1  # this does NOT change shared_value

# Summary
# --------
# Case	                                             Safe?	   Why
# All threads just read shared_value = 42    	    ✅ Yes	Immutable object is safe to read
# One thread rebinds shared_value = 43 (global)  	❌ No	All threads see updated binding
# One thread copies local_value = shared_value + 1	✅ Yes	Local copy, no shared mutation




# threading.local()
# -----------------
    # It creates a "thread-local storage" object.
    # Each thread can store attributes on it, and they are isolated per thread.

import threading
import uuid
import random
import time
# Create thread-local storage
thread_local_data = threading.local()

def initialize_thread_data():
    thread_local_data.user_id = random.randint(1000, 9999)
    thread_local_data.request_id = str(uuid.uuid4())
    thread_local_data.session_token = f"TOKEN-{random.randint(100000, 999999)}"

def process():
    initialize_thread_data()
    time.sleep(random.random())
    print(f"[{threading.current_thread().name}] user_id = {thread_local_data.user_id}, "
          f"request_id = {thread_local_data.request_id}, "
          f"session_token = {thread_local_data.session_token}")

threads = []
for _ in range(3):
    t = threading.Thread(target=process)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
# o/p
    # [Thread-0] user_id = 4098, request_id = 04efbb7b-ae1f-4b3d-a420-ccf99a3d1e0e, session_token = TOKEN-568921
    # [Thread-2] user_id = 1203, request_id = 5fd15e13-cddb-4f32-83ed-9fa3c6de83e7, session_token = TOKEN-194405
    # [Thread-1] user_id = 8881, request_id = af46eb0f-499f-47aa-aabb-1dc59f070d97, session_token = TOKEN-986421

# Key Notes
    # Think of my_data.value as a per-thread dictionary.
    # Internally, Python stores separate values for each thread behind the scenes.
    # Other threads cannot access the data set by a different thread.

# Use Cases
    # Storing thread-specific configs, caches, or database connections.
    # Avoiding conflicts when threads are working with similar data structures.
    # When using 3rd-party code that isn't thread-safe but can work fine if isolated.

