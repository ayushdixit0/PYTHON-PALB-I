class Solution:
    def maxSubseq(self, s, k):
        stack=[]
        for ch in s:
            while stack and k>0 and ch>stack[-1]:
                stack.pop()
                k-=1
            stack.append(ch)
        
        while k>0:
            stack.pop()
            k-=1
        
        return ''.join(stack)
