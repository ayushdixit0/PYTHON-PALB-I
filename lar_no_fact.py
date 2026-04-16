#Given an integer n, find its factorial. Return a list of integers denoting the digits that make up the factorial of n.

class Solution:
    def factorial(self, n):
        # We start with the factorial of 0 or 1, which is 1
        res = 1
        for i in range(2, n + 1):
            res *= i
            
        # Convert the resulting large integer to a string, 
        # then split into individual digits as integers
        return [int(digit) for digit in str(res)]
