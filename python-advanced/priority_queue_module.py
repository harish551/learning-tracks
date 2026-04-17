'''
Priority Queue Module (heapq)
The heapq module in Python provides an implementation of the heap queue algorithm,
also known as the priority queue algorithm. 

A heap is a binary tree where each parent node is 
less than or equal to its child nodes (for a min-heap) 
or greater than or equal to its child nodes (for a max-heap). 
The heapq module provides functions to maintain the heap property 
and perform operations such as inserting elements, 
removing the smallest element, and finding the smallest element without removing it.
'''

import heapq

# Example of using heapq to create a min-heap
min_heap = []
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 8) 

print(heapq.heappop(min_heap))  # Output: 2 (smallest element)
print(heapq.heappop(min_heap))  # Output: 5
print(heapq.heappop(min_heap))  # Output: 8

# Example of using heapq to create a max-heap by negating the values
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -8)
print(-heapq.heappop(max_heap))  # Output: 8 (largest element)
print(-heapq.heappop(max_heap))  # Output: 5
print(-heapq.heappop(max_heap))  # Output: 2


