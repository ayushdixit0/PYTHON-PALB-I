#Given an array and a range a, b. The task is to partition the array around the range such that the array is divided into three parts.
""" 1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the end.
The individual elements of three sets can appear in any order. You are required to return the modified array. """

class Solution:
    def threeWayPartition(self, arr, a, b):
        n = len(arr)
        low = 0
        mid = 0
        high = n - 1
        
        while mid <= high:
            # Case 1: Element is smaller than the range [a, b]
            if arr[mid] < a:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            
            # Case 2: Element is within the range [a, b]
            elif arr[mid] >= a and arr[mid] <= b:
                mid += 1
                
            # Case 3: Element is greater than the range [a, b]
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                # We don't increment mid here because the swapped element 
                # from high needs to be checked
                high -= 1
        
        return arr
