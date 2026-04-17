'''
Binary Search Pattern

Binary search is an efficient algorithm for finding a target value in a **sorted array**.
It works by repeatedly dividing the search space in half, eliminating half of the remaining
elements with each comparison.

Time Complexity: O(log n)
Space Complexity: O(1) for iterative, O(log n) for recursive (call stack)

Pattern Template:
1. Initialize left and right pointers to array boundaries
2. While left <= right:
    - Calculate mid index
    - Compare mid element with target
    - If match, return mid
    - If target < mid element, search left half (right = mid - 1)
    - If target > mid element, search right half (left = mid + 1)
3. If not found, return -1 (or appropriate sentinel)
'''


def binary_search_iterative(arr, target):
     '''
     Iterative binary search implementation.
     
     Args:
          arr: Sorted list of comparable elements
          target: Value to search for
          
     Returns:
          Index of target if found, else -1
     '''

     left, right = 0, len(arr) - 1
     
     while left <= right:
          mid = (left + right) // 2
          
          if arr[mid] == target:
                return mid
          elif arr[mid] < target:
                left = mid + 1  # Search right half
          else:
                right = mid - 1  # Search left half
     
     return -1


def binary_search_recursive(arr, target, left=0, right=None):
     '''
     Recursive binary search implementation.
     
     Args:
          arr: Sorted list of comparable elements
          target: Value to search for
          left: Left boundary index
          right: Right boundary index
          
     Returns:
          Index of target if found, else -1
     '''

     if right is None:
          right = len(arr) - 1
     
     if left > right:
          return -1
     
     mid = (left + right) // 2
     
     if arr[mid] == target:
          return mid
     elif arr[mid] < target:
          return binary_search_recursive(arr, target, mid + 1, right)
     else:
          return binary_search_recursive(arr, target, left, mid - 1)


# Example usage
if __name__ == '__main__':
     arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
     
     print(f"Array: {arr}")
     print(f"Search for 7 (iterative): {binary_search_iterative(arr, 7)}")
     print(f"Search for 7 (recursive): {binary_search_recursive(arr, 7)}")
     print(f"Search for 20 (not found): {binary_search_iterative(arr, 20)}")