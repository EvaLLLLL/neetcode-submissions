class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[1])

        ans, prevEnd = 0, -float('inf')
        for start, end in intervals:
            if start >= prevEnd:
                prevEnd = end
            else:
                ans += 1

        return ans