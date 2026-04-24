class Solution:
    def factorial(self, n):
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        str1=str(fact)
        list1=list(map(int,str1))
        return list1
