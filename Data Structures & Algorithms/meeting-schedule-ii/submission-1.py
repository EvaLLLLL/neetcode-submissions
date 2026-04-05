"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda interval: interval.start)

        days, prevEnds = 1, [intervals[0].end]
        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            if start < prevEnds[0]:
                days += 1
            else:
                heapq.heappop(prevEnds)
            heapq.heappush(prevEnds, end)
            
        return days
