""" You are given an m x n integer matrix matrix with the following two properties:
• Each row is sorted in non-decreasing order.
• The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity. """

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
            
        m = len(matrix)     # Number of rows
        n = len(matrix[0])  # Number of columns
        
        # Binary search on the virtual 1D array of size m * n
        low = 0
        high = (m * n) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Map 1D mid index to 2D matrix coordinates
            row = mid // n
            col = mid % n
            
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False
