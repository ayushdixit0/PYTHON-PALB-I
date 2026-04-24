class Solution:
    def minParentheses(self, s):
        openc=0
        c=0
        for ch in s:
            if ch =='(':
                openc+=1
            else: #if it's a closing bracket
                if openc>0:
                    openc-=1 #valid pair match
                else:
                    c+=1 #need extra openbracket
        return c+openc#count remanining parentheses
