class Solution:
    def countBalanced(self, arr):
        values=[]
        vowels=set('aeiou')
        for s in arr:
            v=0
            for ch in s:
                if ch in vowels:
                    v+=1
            c=len(s)-v
            values.append(v-c)
        n=len(values)
        count=0
        
        #checking all subarrays
        for i in range(n):
            sum=0
            for j in range(i,n):
                sum+=values[j]
                if sum==0:
                    count+=1
        
        return count
