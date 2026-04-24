#Method1
class Solution:
    def largest(self, arr):
        arr.sort(reverse=True)
        return arr[0]

#Method2
class Solution:
    def largest(self, arr):
        return max(arr)

#Method3
class Solution:
    def largest(self, arr):
        max=arr[0]
        for i in arr:
            if i>max:
                max=i
        return max
            
