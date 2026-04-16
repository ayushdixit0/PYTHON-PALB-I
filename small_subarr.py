#Given a number x and an array of integers arr, find the smallest subarray with sum greater than the given value. If such a subarray do not exist return 0 in that case.

class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        # Initialize current sum and minimum length
        current_sum = 0
        min_len = n + 1
        
        # Start and end pointers for the sliding window
        start = 0
        end = 0
        
        while end < n:
            # Keep adding array elements while current sum is less than or equal to x
            while current_sum <= x and end < n:
                current_sum += arr[end]
                end += 1
            
            # Once current sum becomes greater than x, try shrinking the window 
            # from the left to find a smaller subarray
            while current_sum > x and start < n:
                # Update minimum length if a smaller length is found
                if end - start < min_len:
                    min_len = end - start
                
                # Remove starting elements
                current_sum -= arr[start]
                start += 1
                
        # If min_len was never updated, no such subarray exists
        return min_len if min_len <= n else 0
