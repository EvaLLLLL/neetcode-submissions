class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        memo = {}

        def dfs(r, c, prev):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                matrix[r][c] <= prev
            ):
                return 0

            if (r, c) in memo:
                return memo[(r, c)]
            
            best = 1
            for dr, dc in DIRECTIONS:
                best = max(best, 1 + dfs(r + dr, c + dc, matrix[r][c]))

            memo[(r, c)] = best
            return best

        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                ans = max(ans, dfs(r, c, -1))
        return ans
