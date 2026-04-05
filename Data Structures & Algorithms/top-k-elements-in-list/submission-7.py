class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        mp = []
        for v, c in freq.items():
            heapq.heappush(mp, (-c, v))
        
        output = []
        for i in range(k):
            c, v = heapq.heappop(mp)
            output.append(v)
        return output