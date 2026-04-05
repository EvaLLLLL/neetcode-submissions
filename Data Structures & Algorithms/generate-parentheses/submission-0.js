class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n) {
  let res = []
  let stack = []

  function backtrack(openNum, closeNum) {
    if (openNum === closeNum && openNum === n) {
      res.push(stack.join(''))
      return
    }

    if (openNum < n) {
      stack.push('(')
      backtrack(openNum + 1, closeNum)
      stack.pop()
    }

    if (closeNum < openNum) {
      stack.push(')')
      backtrack(openNum, closeNum + 1)
      stack.pop()
    }
  }

  backtrack(0, 0)

  return res
    }
}
