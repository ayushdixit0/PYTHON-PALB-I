# You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].

class Solution:
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubarraySum(self, arr):
        # 1. Initialize variables with the first element
        # current_max tracks the max sum ending at the current position
        # max_so_far tracks the overall maximum found
        current_max = arr[0]
        max_so_far = arr[0]
        
        # 2. Iterate through the array starting from the second element
        for i in range(1, len(arr)):
            # Decision: Should we add the current element to the existing sum, 
            # or start a new subarray from this element?
            current_max = max(arr[i], current_max + arr[i])
            
            # Update the global maximum
            if current_max > max_so_far:
                max_so_far = current_max
                
        return max_so_far
        
