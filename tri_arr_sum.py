#Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target. Return true if such a triplet exists, otherwise, return false.

class Solution:
    def hasTripletSum(self, arr, target):
        n = len(arr)
        # 1. Sort the array
        arr.sort()
        
        # 2. Iterate through the array, fixing one element at a time
        for i in range(n - 2):
            # To handle duplicates (optional but good practice):
            # if i > 0 and arr[i] == arr[i-1]: continue
            
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                
                if current_sum == target:
                    return True
                
                elif current_sum < target:
                    left += 1  # Need a larger sum
                else:
                    right -= 1 # Need a smaller sum
                    
        return False
