from collections import Counter
import heapq

def top_k_frequent(nums, k):
    freq = Counter(nums)
    heap = []
    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for _, num in sorted(heap)]

nums = [1,3,3,3,3,4,5,6,8,1,4,2,8,8,1,1,1]
print(f'Top 3 Frequest Numbers: {top_k_frequent(nums, 3)}')

# Time Complexity O(n log k) with sort O(k log k) Total: O(n log k)
# Space Complexity O(k)
