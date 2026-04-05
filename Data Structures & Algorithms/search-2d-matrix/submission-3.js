class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
          if (!matrix.length) return false

  let top = 0
  let bot = matrix.length - 1

  let rowIndex = -1
  while (top <= bot) {
    let m = Math.floor(top + (bot - top) / 2)
    let min = matrix[m][0]
    let max = matrix[m][matrix[m].length - 1]
    if (target > max) {
      top = m + 1
    } else if (target < min) {
      bot = m - 1
    } else {
      rowIndex = m
      break
    }
  }

  if (rowIndex < 0) return false

  let l = 0
  let r = matrix[rowIndex].length - 1

  while (l <= r) {
    let m = Math.floor(l + (r - l) / 2)
    if (target > matrix[rowIndex][m]) {
      l = m + 1
    } else if (target < matrix[rowIndex][m]) {
      r = m - 1
    } else {
      return true
    }
  }

  return false
    }
}
