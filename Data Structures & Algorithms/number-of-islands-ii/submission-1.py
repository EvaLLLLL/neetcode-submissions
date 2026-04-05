class UnionFind:
    def __init__(self, size):
        self.parent = [-1] * size
        self.rank = [0] * size
        self.count = 0

    def add_land(self, x):
        if self.parent[x] >= 0:
            return

        self.parent[x] = x
        self.count += 1

    def is_land(self, x):
        if self.parent[x] >= 0:
            return True
        else:
            return False
    
    def number_of_islands(self):
        return self.count

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2: return

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1

        self.count -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dsu = UnionFind(m * n)
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        res = []
        for pos in positions:
            r, c = pos
            cell = r * n + c
            if not dsu.is_land(cell):
                dsu.add_land(cell)

                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    nextCell = nr * n + nc
                    if 0 <= nr < m and 0 <= nc < n and dsu.is_land(nextCell):
                        dsu.union(cell, nextCell)

            res.append(dsu.number_of_islands())
        
        return res
