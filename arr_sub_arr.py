#Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[]

from collections import Counter

class Solution:
    def isSubset(self, a, b):
        # 1. Count frequencies of elements in array a
        counts_a = Counter(a)
        
        # 2. Check each element of b against the counts
        for x in b:
            if counts_a[x] > 0:
                counts_a[x] -= 1
            else:
                # Element not in a OR not enough occurrences
                return False
                
        return True
