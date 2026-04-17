'''
Shared memory in Python multiprocessing
Shared memory allows multiple processes to access the same memory space, 
enabling efficient communication and data sharing between processes 
without the need for serialization or inter-process communication (IPC) mechanisms.
'''

import multiprocessing
import time

def increment(shared_value):
    with shared_value.get_lock():  # Ensure atomic access to shared value
        shared_value.value += 1

if __name__ == "__main__":
    shared_value = multiprocessing.Value('i', 0)  # 'i' for integer, initial value 0
    processes = [multiprocessing.Process(target=increment, args=(shared_value,)) for _ in range(5)]

    start = time.time()
    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f'Final shared value: {shared_value.value}')  # Should be 5
    print(f'Time taken: {time.time() - start:.2f} seconds')