class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mp = []

        for point in points:
            d = point[0]**2 + point[1]**2
            heapq.heappush(mp, (d, point))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(mp)[1])

        return res