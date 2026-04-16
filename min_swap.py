# Given an array arr and a number k. One can apply a swap operation on the array any number of times, i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] . Find the minimum number of swaps required to bring all the numbers less than or equal to k together, i.e. make them a contiguous subarray

class Solution:
    def minSwap(self, arr, k):
        n = len(arr)
        
        # Step 1: Count elements <= k (this is our window size)
        fav = 0
        for i in range(n):
            if arr[i] <= k:
                fav += 1
        
        # If no elements or only one element is <= k, no swaps needed
        if fav <= 1:
            return 0
            
        # Step 2: Count elements > k in the first window of size 'fav'
        bad = 0
        for i in range(fav):
            if arr[i] > k:
                bad += 1
        
        ans = bad
        
        # Step 3: Use sliding window to check other windows
        # i is the start of the previous window, j is the end of the current window
        i = 0
        j = fav
        while j < n:
            # Remove the effect of the element going out of the window
            if arr[i] > k:
                bad -= 1
            
            # Add the effect of the element coming into the window
            if arr[j] > k:
                bad += 1
            
            # Update minimum swaps needed
            ans = min(ans, bad)
            
            i += 1
            j += 1
            
        return ans
