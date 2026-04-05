class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def checkBoarder(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS):
                return
            if board[r][c] != "O":
                return
            
            board[r][c] = "B"
            checkBoarder(r + 1, c)
            checkBoarder(r - 1, c)
            checkBoarder(r, c + 1)
            checkBoarder(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                    if board[r][c] == "O":
                        checkBoarder(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "B":
                    board[r][c] = "O"
        
