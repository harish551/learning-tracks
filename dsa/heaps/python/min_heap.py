import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)

print(heap)  # [2, 5, 8]


# pop smallest element
print(heapq.heappop(heap))

# heapify
nums = [2,6,1,0,3,4]
heapq.heapify(nums)
print(nums)

#push and pop
heapq.heappushpop(nums, 7)
print(nums)

# pop push
heapq.heapreplace(nums, 0)
print(nums)

print("Top 3 elements: ", heapq.nlargest(3, nums))
print("Small 3 elements: ", heapq.nsmallest(3, nums))

# custom Priority ordered by first element
nums = [(3, 4),(1, 5),(2, 1)]
print("Before: ", nums)
heapq.heapify(nums)
print("After: ", nums)