import heapq

def find_kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]

nums = [1,5,3,2,8,9]
print(f'nums {nums}, 3rd largest is {find_kth_largest(nums, 3)}')
# Time Complexity: O(n log k)
# Space Complexity O(k)

# using heapq.nlargest
print(f'nums {nums}, 3rd largest is {heapq.nlargest(3,nums)[-1]}')