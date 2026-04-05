class Solution {
    /**
     * @param {number[][]} grid
     */
    islandsAndTreasure(grid) {
          const ROWS = grid.length
  const COLS = grid[0].length

  let queue = []

  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
      if (grid[r][c] === 0) {
        queue.push([r, c])
      }
    }
  }

  const directions = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
  ]
  const visited = new Set()
  let steps = 1

  while (queue.length) {
    const size = queue.length

    for (let i = 0; i < size; i++) {
      const [r, c] = queue.shift()
      for (const [dr, dc] of directions) {
        const row = r + dr
        const col = c + dc

        if (
          row >= 0 &&
          row < ROWS &&
          col >= 0 &&
          col < COLS &&
          grid[row][col] > 0 &&
          !visited.has(`${row}-${col}`)
        ) {
          visited.add(`${row}-${col}`)
          grid[row][col] = steps
          queue.push([row, col])
        }
      }
    }

    steps++
  }
    }
}
