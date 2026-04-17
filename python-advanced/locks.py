'''
Locks in Python are synchronization primitives
that are used to control access to shared resources in a multi-threaded environment.
'''

import threading

# Example of using a lock to protect a shared resource
counter = 0
counter_lock = threading.Lock()
def increment_counter():
    global counter
    with counter_lock:  # Acquire lock before modifying the counter
        for _ in range(100000):
            counter += 1  # Critical section

threads = [threading.Thread(target=increment_counter) for _ in range(5)]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f'Final counter value: {counter}')  # Should be 500000