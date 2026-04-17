'''
Given an array with integers in sorted order 
Return indexes (1-based indexing) of elements whose sum matches target

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Approach:
Two-Pointer 
'''

from typing import List

def two_sum(numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers)-1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1, r+1]
        if s > target:
            r -= 1
        else:
            l += 1
    return []

print(two_sum([2,7,11,15], 9))