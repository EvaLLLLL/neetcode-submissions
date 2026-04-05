class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        l, r = 0, len(intervals) - 1

        while l <= r:
            m = (l + r) // 2
            target = intervals[m][0]
            if target >= newInterval[0]:
                r = m - 1
            else:
                l = m + 1

        
        intervals.insert(l, newInterval)
        output = []

        for start, end in intervals:
            if not output or start > output[-1][1]:
                output.append([start, end])
            else:
                output[-1][1] = max(output[-1][1], end)
        
        return output