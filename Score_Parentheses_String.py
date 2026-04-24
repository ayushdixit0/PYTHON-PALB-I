#Method1
class Solution:
    def scoreOfParentheses(self, s):
        score=0
        layer=0
        for i in range(len(s)):
            if s[i]=='(':
                layer+=1
            else:
                layer-=1
                if s[i-1]=='(': #() found
                    score+=2**layer
        return score

#Method 2
class Solution:
    def scoreOfParentheses(self, s):
        score=0
        layer=0
        power=1
        for i in range(len(s)):
            if s[i]=='(':
                layer+=1
                power*=2
            else:
                layer-=1
                power//=2
                if s[i-1]=='(': #() found
                    score+=power
        return score
