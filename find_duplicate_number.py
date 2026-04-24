class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1={}
        for i in nums:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for i in dict1:
            if dict1[i]>1:
                return i
