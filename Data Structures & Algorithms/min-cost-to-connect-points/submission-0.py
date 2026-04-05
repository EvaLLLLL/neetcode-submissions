class DSU:
    def __init__(self, n):
        self.Parent = list(range(n))
        self.Size = [1] * (n)
    
    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Size[pu] > self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                w = abs(xi - xj) + abs(yi - yj)
                edges.append((w, i, j))

        edges.sort()

        ans = 0
        dsu = DSU(n)
        for w, u, v in edges:
            if dsu.union(u, v):
                ans += w
        
        return ans
