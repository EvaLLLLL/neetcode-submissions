class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
                     
        def dfs(i, j):
            if (
                i < 0 or
                j < 0 or
                i >= ROWS or
                j >= COLS or
                grid[i][j] == 0
            ):
                return 1

            if (i, j) in visit:
                return 0
            
            visit.add((i, j))
            perim = 0
            for dr, dc in DIRECTIONS:
                perim += dfs(i + dr, j + dc)
            return perim

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    return dfs(r, c)

        return 0