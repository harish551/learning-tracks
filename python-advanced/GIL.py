'''
The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects,
preventing multiple threads from executing Python bytecode at the same time.

The GIL is necessary because CPython's memory management is not thread-safe.
While the GIL simplifies memory management and ensures thread safety,
it can be a bottleneck for CPU-bound multi-threaded programs,
as only one thread can execute Python code at a time.

However, for I/O-bound tasks, the GIL is less of an issue,
as threads can release the GIL while waiting for I/O operations to complete,
allowing other threads to run.
'''

import threading
import time


def worker(num):
    print(f'Thread {num} starting')
    time.sleep(1)
    print(f'Thread {num} finished')

threads = [ threading.Thread(target=worker, args=(i,)) for i in range(5) ]

start = time.time()
for t in threads:
    t.start()

for t in threads:
    t.join()

print(f'All threads completed in {time.time() - start:.2f} seconds')


# Examples of Locking and Releasing GIL
import threading
import time

def cpu_bound_task():
    print("Starting CPU-bound task")
    total = 0
    for i in range(10**7):
        total += i
    print("Finished CPU-bound task")

def io_bound_task():
    print("Starting I/O-bound task")
    time.sleep(2)
    print("Finished I/O-bound task")

# Create threads for CPU-bound and I/O-bound tasks
cpu_threads = [threading.Thread(target=cpu_bound_task) for _ in range(3)]
io_threads = [threading.Thread(target=io_bound_task) for _ in range(3)]

for thread in cpu_threads:
    thread.start()

for thread in io_threads:
    thread.start()

for thread in cpu_threads:
    thread.join()

for thread in io_threads:
    thread.join()