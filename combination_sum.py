class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        curr=[]
        def backtrack(i,curr,target):
            if target==0:
                result.append(curr[:])
                return
            if target<0:
                return
            for j in range(i,len(candidates)):
                curr.append(candidates[j])
                backtrack(j,curr,target-candidates[j])
                curr.pop()#backtracking
        backtrack(0,curr,target)
        return result
