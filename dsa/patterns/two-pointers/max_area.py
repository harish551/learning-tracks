from typing import List


'''
Given Heights of vertical lines on x-axis 

Find a container area with most water 

Approch:
 use two pointer variable from opposite ends left & right
 check area with minimum height multiplied with difference of positions on x-axis (indexes)
 which gives rectangle area (water filled)
 track maxArea untile both ends meet
'''


def maxArea(height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    ans = 0
    while l < r:
        water = min(height[l], height[r]) * (r-l)
        ans = max(ans, water)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return ans