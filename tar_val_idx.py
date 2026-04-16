#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store: { value: index }
        prev_map = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            
            # Check if the needed number has already been seen
            if diff in prev_map:
                return [prev_map[diff], i]
            
            # Store the current number's index for future reference
            prev_map[n] = i
            
        return []
