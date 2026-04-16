#Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.

import heapq

class Solution:
    def kthSmallest(self, arr, k):
        # Python's heapq is a min-heap by default.
        # To use it as a max-heap, we store negative values.
        max_heap = []
        
        for num in arr:
            heapq.heappush(max_heap, -num)
            # If heap size exceeds k, pop the largest element
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        # The root is the kth smallest (remember to flip the sign back)
        return -max_heap[0]
