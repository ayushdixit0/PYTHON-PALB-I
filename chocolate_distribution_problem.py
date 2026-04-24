class Solution:

    def findMinDiff(self, arr,M):
        n=len(arr)
        arr.sort()
        mindiff=arr[M-1]-arr[0]
        for i in range(1,n-M+1):
            currdiff=arr[i+M-1]-arr[i]
            mindiff=min(mindiff,currdiff)
        return mindiff
