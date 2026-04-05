class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        for cnt, ch in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if cnt != 0:
                heapq.heappush(maxHeap, (cnt, ch))

        res = ""

        while maxHeap:
            cnt1, ch1 = heapq.heappop(maxHeap)

            if len(res) >= 2 and ch1 == res[-1] == res[-2]:
                if not maxHeap:
                    break
                cnt2, ch2 = heapq.heappop(maxHeap)
                res += ch2
                cnt2 += 1
                if cnt2 != 0:
                    heapq.heappush(maxHeap, (cnt2, ch2))
                heapq.heappush(maxHeap, (cnt1, ch1))
            else:
                res += ch1
                cnt1 += 1
                if cnt1 != 0:
                    heapq.heappush(maxHeap, (cnt1, ch1))
        return res
        