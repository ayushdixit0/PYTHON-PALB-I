from math import factorial
class Solution:
    def vowelCount(self, s): #frequencies of distinct vowels * factorial
        vowels=['a','e','i','o','u']
        freq={v:0 for v in vowels}
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        
        product=1
        v=0 #for counting distinct vowels
        
        for i in vowels:
            if freq[i]>0:
                product*=freq[i]
                v+=1
        
        if v==0:
            return 0
            
        return product*factorial(v)
