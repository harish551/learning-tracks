import heapq

nums = [8,1,2,9,6,4]

heap = []
for num in nums:
    heapq.heappush(heap, -num)

while heap:
    print(-heapq.heappop(heap), end=", ")
print()


