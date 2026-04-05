class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for s, d, w in edges:
            adj[s].append([w, d])
            adj[d].append([w, s])

        total = 0
        minHeap = []
        visited = set()
        visited.add(0)

        for w1, d1 in adj[0]:
            heapq.heappush(minHeap, [w1, d1])

        while minHeap:
            w2, d2 = heapq.heappop(minHeap)

            if d2 in visited:
                continue

            total = total + w2
            visited.add(d2)

            for w3, d3 in adj[d2]:
                heapq.heappush(minHeap, [w3, d3])
        
        return total if len(visited) == n else -1
        