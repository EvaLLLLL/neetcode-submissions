class Solution {
    /**
     * @param {character[][]} board
     * @return {void} Do not return anything, modify board in-place instead.
     */
    solve(board) {
        const ROWS = board.length
        const COLS = board[0].length

        const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        const capture = (r, c) => {
            if (
                r < 0 || 
                c < 0 ||
                r === ROWS ||
                c === COLS || 
                board[r][c] !== "O"
            ) return

            board[r][c] = "T"

            for (let [dr, dc] of directions) {
                capture(r + dr, c + dc)
            }
        }

        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                if ([0, ROWS - 1].includes(r) || [0, COLS - 1].includes(c)) {
                    capture(r, c)
                }
            }
        }

        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                if (board[r][c] === "O") {
                    board[r][c] = "X"
                }
            }
        }

        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                if (board[r][c] === "T") {
                    board[r][c] = "O"
                }
            }
        }
    }
}
