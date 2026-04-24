#Method1
class Solution:
    def sortByLength(self, arr):
       arr.sort(key=len)

#Method 2 using Insertion Sort because it is stable
class Solution:
    def sortByLength(self, arr):
        n=len(arr)
        for i in range(1,n):
            key=arr[i]
            j=i-1
            while j>=0 and len(arr[j])>len(key):
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
        return arr
