class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        stack = [intervals[0]]
        for start, end in intervals[1:]:
            if stack and start <= stack[-1][1]:
                prevStart, prevEnd = stack.pop()
                stack.append([prevStart, max(end, prevEnd)])
            else:
                stack.append([start, end])
        return stack