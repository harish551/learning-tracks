'''
Concurrency is the ability of a program to manage multiple tasks at the same time.

Concurrency in Python can be achieved through various mechanisms, 
including threading, multiprocessing, and asynchronous programming. 

Each of these approaches has its own advantages and use cases.
'''

# Example of concurrency using asynchronous programming with asyncio
import asyncio
import time

async def task():
    print("Hello")
    await asyncio.sleep(1)

asyncio.run(task())

# Example of real-world problem concurrency with asyncio
import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulate I/O-bound operation
    print("Data fetched")

async def main():
    
    await asyncio.gather(fetch_data(), fetch_data())

start = time.time()
asyncio.run(main()) 
print(f"Total time taken: {time.time() - start:.2f} seconds")