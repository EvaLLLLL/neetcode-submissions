class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        visit = set() # (row, col)
        distinct = set() # 
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, direction, path):
            if (
                r < 0 or 
                r >= ROWS or
                c < 0 or
                c >= COLS or
                (r, c) in visit or
                grid[r][c] == 0
            ):
                return

            visit.add((r, c))
            grid[r][c] = 0
            path.append(direction)
            dfs(r + 1, c, "D", path)
            dfs(r - 1, c, "U", path)
            dfs(r, c + 1, "R", path)
            dfs(r, c - 1, "L", path)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == 1:
                    path = []
                    dfs(r, c, "GO", path)
                    if path:
                        distinct.add(tuple(path))

        return len(distinct)

            
