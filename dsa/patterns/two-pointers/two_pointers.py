'''
Two Pointers:

Use two indices to traverse data (usually arrays/strings) efficiently instead of nested loops.

When to use:
 - sorted array / strings
 - pairs / triplets
 - remove duplicates
 - sliding window variants
'''

# Template
from typing import List


# Opposite ends left, right
def two_pointers(arr: List[int], target: int) -> List[int]:
    l, r = 0, len(arr) - 1
    while l < r:
        s = arr[l] + arr[r]
        if s == target:
            return [l, r]
        elif s < target:
            l += 1
        else:
            r -= 1
    return []

