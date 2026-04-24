#User function Template for python3
class Solution:
    def search(self, txt, pat):
        n=len(pat)
        pat1=sorted(pat)
        for i in range(len(txt)-n+1):
            if sorted(txt[i:i+n])==pat1:
                return True
        return False
