class Solution:
    def maxSubarraySum(self, arr):
        maxsum=arr[0]
        currsum=arr[0]
        for i in range(1,len(arr)):
            currsum=max(arr[i],currsum+arr[i])
            maxsum=max(maxsum,currsum)
        return maxsum
