class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1):
            ndist = dist[:]
            for u, v, w in flights:
                if dist[u] == float('inf'):
                    continue
                if dist[u] + w < ndist[v]:
                    ndist[v] = dist[u] + w
            dist = ndist
        
        return -1 if dist[dst] == float('inf') else dist[dst]