# Given an array arr[] of integers, calculate the median.

class Solution:
    def findMedian(self, arr):
        n = len(arr)
        # 1. Sort the array
        arr.sort()
        
        # 2. If length is odd, return middle element
        if n % 2 != 0:
            return float(arr[n // 2])
        
        # 3. If length is even, return average of two middle elements
        else:
            mid1 = arr[n // 2]
            mid2 = arr[(n // 2) - 1]
            return (mid1 + mid2) / 2.0
