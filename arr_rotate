# Given an array arr, rotate the array by one position in clockwise direction.

class Solution:
    def rotate(self, arr):
        # 1. Get the length of the array
        n = len(arr)
        
        # Guard clause: if array is empty or has 1 element, no rotation needed
        if n <= 1:
            return
            
        # 2. Store the last element so it doesn't get lost
        last_element = arr[n - 1]
        
        # 3. Shift elements to the right
        # We start from the end and move backwards to index 1
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]
            
        # 4. Place the saved last element at the first position (index 0)
        arr[0] = last_element
