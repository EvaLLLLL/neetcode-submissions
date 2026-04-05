class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for q in queries:
            l = float('inf')
            for start, end in intervals:
                if start <= q <= end:
                    l = min(end - start + 1, l)
            res.append(l if l != float('inf') else -1)
        return res

