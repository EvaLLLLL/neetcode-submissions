class Solution {
    /**
     * @param {number[][]} grid
     * @returns {number}
     */
    countPaths(grid) {
        let visit = new Set()
        return this.dfs(grid, 0, 0, visit)
    }

    dfs(grid, r, c, visit) {
        const ROWS = grid.length
        const COLS = grid[0].length

        if (r < 0 || c < 0) return 0
        if (r === ROWS || c === COLS) return 0 
        if (visit.has(`${r}${c}`)) return 0
        if (grid[r][c] === 1) return 0

        if (r === ROWS - 1 && c === COLS - 1) return 1

        visit.add(`${r}${c}`)

        let count = 0
        count += this.dfs(grid, r + 1, c, visit)
        count += this.dfs(grid, r - 1, c, visit)
        count += this.dfs(grid, r, c + 1, visit)
        count += this.dfs(grid, r, c - 1, visit)

        visit.delete(`${r}${c}`)
        return count
    }
}
