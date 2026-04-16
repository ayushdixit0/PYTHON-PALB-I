#You are given a rectangular matrix mat[][] of size n x m, and your task is to return an array while traversing the matrix in spiral form.

class Solution:
    def spirallyTraverse(self, mat):
        if not mat or not mat[0]:
            return []
            
        n = len(mat)
        m = len(mat[0])
        
        # Initialize boundaries
        top = 0
        bottom = n - 1
        left = 0
        right = m - 1
        
        result = []
        
        while top <= bottom and left <= right:
            # 1. Move Right: Traverse top row
            for j in range(left, right + 1):
                result.append(mat[top][j])
            top += 1
            
            # 2. Move Down: Traverse right column
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1
            
            # 3. Move Left: Traverse bottom row (if still valid)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(mat[bottom][j])
                bottom -= 1
            
            # 4. Move Up: Traverse left column (if still valid)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1
                
        return result
