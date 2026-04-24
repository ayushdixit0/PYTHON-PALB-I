class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=-1
        right=-1

        #finding first position
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                left=mid
                high=mid-1 #to search left part repeatedly
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        
        #finding last position
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                right=mid
                low=mid+1 #to search right part repeatedly
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1

        return [left,right]
