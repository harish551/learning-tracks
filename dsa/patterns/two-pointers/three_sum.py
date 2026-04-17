'''
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Approach:
- sort array to effectively ignore duplicates
- iterate over elemets for every i check different j and k values 
- check if sum == 0 if yes append nums at i,j,k to result aray and move j and k pointers 
- all duplicates will be side by side in sorted array
     so if next element matches with prev one continue to next
- if sum > 0 we should move pointer from right side (k) since last elements are bigger values compare to j
- if sum < 0 we should move pointer from left side (j) it may have nagative values 
- repeat this until n-2 elements
'''
from typing import List

# Time Complexity: O(n^2)
# Space Complexity: O(n)
def three_sum(nums: List[int]) -> List[List[int]]:
    if not nums or len(nums) < 3:
        return []
    
    n = len(nums)
    result = []
    nums.sort()

    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j = i+1
        k = n-1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s == 0:
                result.append([nums[i], nums[j], nums[k]])

                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                
            elif s > 0:
                k -= 1

            else:
                j += 1

    return result

print(three_sum([-1,0,1,2,-1,-4]))
            
            


