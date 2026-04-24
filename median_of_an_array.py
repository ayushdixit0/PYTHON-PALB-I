class Solution:
    def findMedian(self, arr):
        arr.sort()
        n=len(arr)
        mid=len(arr)//2
        if n%2!=0:
            return arr[mid]
        else:
            return (arr[mid-1]+arr[mid])/2
