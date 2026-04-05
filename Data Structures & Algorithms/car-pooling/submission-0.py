class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        for num, start, end in trips:
            heapq.heappush(heap, (start, num))
            heapq.heappush(heap, (end, -num))

        cap = 0
        while heap:

            cap += heapq.heappop(heap)[1]
            if cap > capacity:
                return False 

        return True
