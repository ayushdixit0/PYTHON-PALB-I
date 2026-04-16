#Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without using any extra space. Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.


class Solution:
    def mergeArrays(self, a, b):
        n = len(a)
        m = len(b)
        
        i = n - 1  # Last element of a
        j = 0      # First element of b
        
        # Swap elements if they are in the wrong array
        while i >= 0 and j < m:
            if a[i] > b[j]:
                a[i], b[j] = b[j], a[i]
                i -= 1
                j += 1
            else:
                # Since arrays are sorted, if a[i] <= b[j], 
                # all elements before i are also smaller than b[j]
                break
        
        # Now that both arrays have the correct elements, 
        # sort them to restore order.
        a.sort()
        b.sort()
