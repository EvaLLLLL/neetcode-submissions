class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = []
        for n, cnt in freq.items():
            heapq.heappush(heap, (-cnt, n))

        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res
