class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result=[]
        curr=[]
        def backtrack(i,curr,target):
            if target==0:
                result.append(curr[:])
                return
            if target<0:
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                curr.append(candidates[j])
                backtrack(j+1,curr,target-candidates[j])
                curr.pop()#backtracking
        backtrack(0,curr,target)
        return result
