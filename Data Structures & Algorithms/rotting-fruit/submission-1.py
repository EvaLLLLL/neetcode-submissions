class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        queue = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        time = 0
        while fresh and queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
            
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc

                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1):
                        continue

                    fresh -= 1
                    grid[nr][nc] = 2
                    queue.append((nr, nc))
            time += 1
        return time if fresh == 0 else -1