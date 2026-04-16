#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        # 1. Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        merged = []
        
        for interval in intervals:
            # If merged is empty or no overlap, append the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is an overlap, so merge the current interval 
                # with the previous one by updating the end time
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
