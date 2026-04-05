class Solution {
    /**
     * @param {number[][]} heights
     * @return {number[][]}
     */
    pacificAtlantic(heights) {
        const ROWS = heights.length
        const COLS = heights[0].length
        const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        let pac = Array.from({length: ROWS}, () => Array(COLS).fill(false))
        let alt = Array.from({length: ROWS}, () => Array(COLS).fill(false))
       
        const dfs = (r, c, ocean) => {
            ocean[r][c] = true

            for (let [dr, dc] of directions) {
                let nr = r + dr
                let nc = c + dc
                if (
                    nr >= 0 &&
                    nc >= 0 &&
                    nr < ROWS &&
                    nc < COLS &&
                    !ocean[nr][nc] &&
                    heights[nr][nc] >= heights[r][c]
                ) {
                    dfs(nr, nc, ocean)
                }
            }
        }

        for (let c = 0; c < COLS; c++) {
            dfs(0, c, pac)
            dfs(ROWS - 1, c, alt)
        }

        for (let r = 0; r < ROWS; r++) {
            dfs(r, 0, pac)
            dfs(r, COLS - 1, alt)
        }

        let res = []
        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                if (pac[r][c] && alt[r][c]) {
                    res.push([r, c])
                }
            }
        }

        return res
    }
}
