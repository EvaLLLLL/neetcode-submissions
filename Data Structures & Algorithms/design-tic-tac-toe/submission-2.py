class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        isColumn = all(self.board[r][col] == player for r in range(self.n))
        if isColumn:
            return player

        isRow = all(self.board[row][c] == player for c in range(self.n))
        if isRow:
            return player

        isPosDiagonal = all(self.board[i][i] == player for i in range(self.n))
        if isPosDiagonal:
            return player

        isNegDiagonal = all(self.board[i][self.n - i - 1] == player for i in range(self.n))
        if isNegDiagonal:
            return player

        return 0


    


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)