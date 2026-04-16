# Given a row-wise sorted matrix mat[][] of size n*m, where the number of rows and columns is always odd. Return the median of the matrix.

from bisect import bisect_right

class Solution:
    def median(self, matrix):
        # The driver only passes the matrix
        # We calculate R (rows) and C (columns) ourselves
        R = len(matrix)
        C = len(matrix[0])
        
        low = float('inf')
        high = float('-inf')
        
        # Find the min and max values in the matrix for the binary search range
        for i in range(R):
            low = min(low, matrix[i][0])
            high = max(high, matrix[i][C-1])
            
        # The position of the median (always odd total elements per problem description)
        desired = (R * C + 1) // 2
        
        while low <= high:
            mid = low + (high - low) // 2
            count = 0
            
            # Count elements <= mid across all rows
            for i in range(R):
                count += bisect_right(matrix[i], mid)
            
            if count < desired:
                low = mid + 1
            else:
                high = mid - 1
                
        return low
