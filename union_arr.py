#You are given two arrays a[] and b[], return the Union of both the arrays in any order.

class Solution:    
    # Function to return the union of two arrays.
    def findUnion(self, a, b):
        # 1. Create a set from the first array (removes duplicates)
        set_a = set(a)
        
        # 2. Create a set from the second array (removes duplicates)
        set_b = set(b)
        
        # 3. Use the union operator (|) to combine them
        union_set = set_a | set_b
        
        # 4. Return as a list (GFG driver code will sort it for you)
        return list(union_set)
