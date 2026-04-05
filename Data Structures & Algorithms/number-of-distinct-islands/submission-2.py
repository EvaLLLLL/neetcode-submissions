class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, direction, path):
            if (
                r < 0 or 
                r >= ROWS or
                c < 0 or
                c >= COLS or
                grid[r][c] == 0
            ):
                return

            grid[r][c] = 0
            path.append(direction)
            dfs(r + 1, c, "D", path)
            dfs(r - 1, c, "U", path)
            dfs(r, c + 1, "R", path)
            dfs(r, c - 1, "L", path)

        distinct = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    path = []
                    dfs(r, c, "GO", path)
                    if path:
                        distinct.add(tuple(path))

        return len(distinct)

            
