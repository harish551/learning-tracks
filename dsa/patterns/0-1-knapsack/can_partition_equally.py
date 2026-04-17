from typing import List

def canPartitionBitmask(nums: List[int]) -> bool:
    total = sum(nums)
    if total & 1:
        return False
    target = total // 2
    bitmask = 1 << target
    for n in nums:
        bitmask |= bitmask >> n

    return bool(bitmask & 1)

print(canPartitionBitmask([8,10]))