#Given an array arr[] denoting heights of n towers and a positive integer k.

class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0
            
        # 1. Sort the array to handle heights greedily
        arr.sort()
        
        # 2. Baseline answer (difference between tallest and shortest)
        ans = arr[n-1] - arr[0]
        
        # 3. Iterate through the array to find a better split point
        for i in range(n - 1):
            # We increase towers from 0 to i by k
            # We decrease towers from i+1 to n-1 by k
            
            # The potential new maximum
            high = max(arr[i] + k, arr[n-1] - k)
            
            # The potential new minimum
            low = min(arr[0] + k, arr[i+1] - k)
            
            # The problem states heights cannot be negative
            if low < 0:
                continue
            
            # Update the minimum difference found so far
            ans = min(ans, high - low)
            
        return ans
