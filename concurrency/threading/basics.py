# threading.Thread(target=worker, args=(i,), daemon=True)
# threading.Lock()

# sem1 = threading.Semaphore(count)
# sem1.acquire()
# sem1.release()

# b1 = threading.Barrier(num_of_threads)
#   is_leader = b1.wait() == False

# Threads 
# Memory Model
# Memory Type	                  Shared Across Threads?	Notes
# Global Variables	              ✅ Yes      	           Must protect with locks if writing
# Heap Objects	                  ✅ Yes                    Shared unless isolated per thread
# Function Locals	              ❌ No	                   Each thread has its own stack (its own local vars)
# # Thread-local Storage	          ❌ No (by design)         Can be implemented using threading.local()


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
# "Lock stops OS from switching threads while one is running"
# This is not true — the OS can still switch context (i.e., pause this thread and schedule another), even if the thread is inside a with lock: block.
# But:
# The lock stays acquired by the original thread, so no other thread can enter the critical section until the original thread releases the lock.
# Even if another thread starts running, when it tries to lock.acquire(), it will block and wait.
