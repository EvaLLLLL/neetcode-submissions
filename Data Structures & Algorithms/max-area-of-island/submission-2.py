class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ans = 0
        visit = set()
        def dfs(r, c):
            if (
                r < 0 or c < 0 or r >= ROW or c >= COL or
                (r, c) in visit or grid[r][c] == 0
            ):
                return 0

            visit.add((r, c))
            res = 1
            for dr, dc in DIRECTIONS:
                res += dfs(r + dr, c + dc)

            return res
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r, c) not in visit:
                    ans = max(ans, dfs(r, c))
        return ans