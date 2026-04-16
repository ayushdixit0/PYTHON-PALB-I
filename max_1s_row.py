# You are given a 2D binary array arr[][] consisting of only 1s and 0s. Each row of the array is sorted in non-decreasing order. Your task is to find and return the index of the first row that contains the maximum number of 1s. If no such row exists, return -1.

class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        if n == 0:
            return -1
        m = len(arr[0])
        
        # Pointer starting at top-right corner
        row = 0
        col = m - 1
        
        max_row_idx = -1
        
        while row < n and col >= 0:
            # If we find a 1, move left to check for a better maximum
            if arr[row][col] == 1:
                max_row_idx = row
                col -= 1
            # If we find a 0, move down to the next row
            else:
                row += 1
                
        return max_row_idx
