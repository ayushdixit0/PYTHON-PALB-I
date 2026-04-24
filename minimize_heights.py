class Solution:
    def getMinDiff(self,arr,k):
        arr.sort()
        n=len(arr)
        mindiff=arr[n-1]-arr[0]
        for i in range(n-1):
            left=min(arr[0]+k,arr[i+1]-k)
            right=max(arr[i]+k,arr[n-1]-k)
            if left<0:
                continue
            mindiff=min(mindiff,right-left)
        return mindiff
            
