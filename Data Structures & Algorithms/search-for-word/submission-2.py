class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        visit = set()
        def backtrack(r, c, i):
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visit or
                board[r][c] != word[i]
            ):
                return False
            
            if i == len(word) - 1:
                return True
            
            visit.add((r, c))
            for dr, dc in DIRECTIONS:
                if backtrack(r + dr, c + dc, i + 1):
                    return True
                
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
                
        return False                    