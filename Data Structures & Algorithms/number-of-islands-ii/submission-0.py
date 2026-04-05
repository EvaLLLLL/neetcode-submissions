class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = [[0] * n for _ in range(m)]

        def dfs(r, c, visit):
            if (r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0 or (r, c) in visit):
                return

            visit.add((r, c))
            dfs(r, c + 1, visit)    
            dfs(r, c - 1, visit)    
            dfs(r + 1, c, visit)    
            dfs(r - 1, c, visit)    

        res = []
        for pos in positions:
            grid[pos[0]][pos[1]] = 1
            island = 0
            visit = set()
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 1 and (r, c) not in visit:
                        dfs(r, c, visit)
                        island += 1
            res.append(island)
        return res