# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive. There is only one repeated number in nums, return this repeated number.
class Solution:
    def findDuplicate(self, nums):
        # Phase 1: Finding the intersection point in the cycle
        tortoise = nums[0]
        hare = nums[0]
        
        while True:
            tortoise = nums[tortoise]      # Move 1 step
            hare = nums[nums[hare]]        # Move 2 steps
            if tortoise == hare:
                break
        
        # Phase 2: Finding the entrance to the cycle (the duplicate)
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]      # Move 1 step
            hare = nums[hare]              # Move 1 step
            
        return hare
