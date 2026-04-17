'''
asyncio is a powerful library in Python that allows you to 
write concurrent code using the async/await syntax. 
It is particularly useful for I/O-bound and high-level structured network code. 

In this example, we will implement a simple producer-consumer pattern using asyncio.
'''

import asyncio

async def producer(queue):
    for i in range(5):
        await asyncio.sleep(1)
        await queue.put(f'Item {i}')
        print(f'Produced {i}')

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f'Consumed {item}')
        queue.task_done()


async def main():
    queue = asyncio.Queue()
    
    # Start producer and consumer tasks
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))
    
    # Wait for the producer to finish producing items
    await producer_task
    
    # Wait until the queue is fully processed
    await queue.join()
    
    # Cancel the consumer task since it's an infinite loop
    consumer_task.cancel()

    queue2 = asyncio.Queue()
    await asyncio.gather(producer(queue2), consumer(queue2))


if __name__ == "__main__":
    asyncio.run(main())