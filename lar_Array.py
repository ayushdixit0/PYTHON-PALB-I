#Given an array arr[]. The task is to find the largest element and return it.

class Solution:
    def largest(self, arr):
        # 1. Handle edge case for empty array
        if not arr:
            return None
            
        # 2. Assume the first element is the largest
        max_val = arr[0]
        
        # 3. Traverse the array and update max_val if a larger number is found
        for num in arr:
            if num > max_val:
                max_val = num
                
        # 4. Return the final largest element
        return max_val
