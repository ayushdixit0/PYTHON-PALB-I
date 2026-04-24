#User function Template for python3
class Solution:

    def winner(self, arr):
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        maxvotes=0
        winnername=''
        for i in freq:
            if freq[i]>maxvotes:
                maxvotes=freq[i]
                winnername=i
            elif freq[i]==maxvotes:
                if i<winnername:
                    winnername=i
        return [winnername,str(maxvotes)]
