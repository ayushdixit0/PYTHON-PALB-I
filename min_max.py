#Given an array arr[]. Your task is to find the minimum and maximum elements in the array.

class Solution:
    def getMinMax(self, arr):
        # Handle empty or null array
        if not arr:
            return []
            
        # Initialize min and max with the first element
        res_min = arr[0]
        res_max = arr[0]
        
        # Traverse the array to find min and max
        for num in arr:
            if num < res_min:
                res_min = num
            if num > res_max:
                res_max = num
                
        # Return as a list or tuple (GFG expects [min, max])
        return [res_min, res_max]
