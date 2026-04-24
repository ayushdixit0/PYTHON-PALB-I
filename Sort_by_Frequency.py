class Solution:
    def frequencySort(self, s):
        freq={}
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        
        #sort by frequency first then lexicographically
        sortedch=sorted(freq.items(), key=lambda x: (x[1],x[0]))
        ans=''
        for ch,frequency in sortedch:
            ans+=ch*frequency
        return ans
