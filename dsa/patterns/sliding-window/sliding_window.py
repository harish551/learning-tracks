'''
Sliding Window

Maintain a window (subarray/substring) and expand/shrink dynamically.

When to use:
- Subarrays / Substrings
- Maximum / Minimum length
- Fixed or Variable window

Time Complexity: O(n)
'''
# sliding window with fixed size k
def sliding_window(arr, k):
    curr_sum = sum(arr[:k])
    max_sum = curr_sum

    for i in range(k, len(arr)):
        curr_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, curr_sum)
    return max_sum

# varible window template - expanding window
def variable_window(s):
    freq = {}
    l = res = 0
    for r, c in enumerate(s):
        freq[c] = freq.get(c, 0) + 1
        while freq[c] > 1:
            freq[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res

from collections import Counter

# variable window -- shrinking window
def min_window_string(s, t):
    if not s or not t:
        return ""
    if len(t) > len(s):
        return ""
        
    need = dict(Counter(t))
    missing = len(t)
    l = start = end = 0
    for r, c in enumerate(s):
        if need.get(c,0) > 0:
            missing -= 1
        need[c] = need.get(c, 0) - 1

        # shrink window until the condition satisfies
        while missing == 0:
            if end == 0 or r - l + 1 < end - start + 1:
                start, end = l, r + 1
                
            need[s[l]] = need.get(s[l], 0) + 1
            if need[s[l]] > 0:
                missing += 1
            l += 1

    return s[start:end]





