class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x: int) -> int:
        p = self.parent[x]
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
            p = self.parent[p]
        return p
    
    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []
        for s, d, w in edges:
            heapq.heappush(minHeap, [w, s, d])

        unionFind = UnionFind(n)
        total, components = 0, 0

        while components < n - 1 and minHeap:
            weight, n1, n2 = heapq.heappop(minHeap)
            if not unionFind.union(n1, n2):
                continue
            total += weight
            components += 1
        return total if components == n - 1 else -1
