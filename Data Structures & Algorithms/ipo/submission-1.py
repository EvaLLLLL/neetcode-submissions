class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        for profit, cap in zip(profits, capital):
            heapq.heappush(heap, (-profit, cap))

        final = w 
        while k:
            cur = []

            if not heap:
                return final

            while heap and heap[0][1] > final:
                p, c = heapq.heappop(heap)
                cur.append((-p, c))

            if not heap:
                return final

            final -= heapq.heappop(heap)[0]

            for p, c in cur:
                heapq.heappush(heap, (-p, c))
            k -= 1
        return final

            
