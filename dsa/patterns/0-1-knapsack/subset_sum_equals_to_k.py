
from typing import List

def subsetSum(nums: List[int], k: int) -> bool:
    n = len(nums)

    if not nums:
        return False
    
    dp = [False] * (k+1)
    dp[0] = True

    for num in nums:
        for i in range(k, num-1, -1):
            dp[i] = dp[i] or dp[i-num]
    return dp[k]

print(subsetSum([2, 3, 7, 8, 10], 11))
print(subsetSum([2, 3, 8, 1], 7))