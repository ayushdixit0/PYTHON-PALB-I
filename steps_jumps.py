#You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.

class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # If the array has only 1 element, you are already at the end
        if n <= 1:
            return 0
        
        # If the first element is 0, you can't move anywhere
        if arr[0] == 0:
            return -1
            
        farthest = 0
        current_end = 0
        jumps = 0
        
        # Traverse the array except for the last element
        # (Once we reach or pass the last element, we stop)
        for i in range(n - 1):
            # Update the farthest point we can reach
            farthest = max(farthest, i + arr[i])
            
            # If we've reached the end of our current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Check if we can already reach the last element
                if current_end >= n - 1:
                    break
        
        # If the end of the array is unreachable
        if current_end < n - 1:
            return -1
            
        return jumps
