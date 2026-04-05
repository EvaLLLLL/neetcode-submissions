class Solution {
    /**
     * @param {string} digits
     * @return {string[]}
     */
    letterCombinations(digits) {
          if (!digits) return []

          const DIGIT_TO_CHAR = {
  '2': 'abc',
  '3': 'def',
  '4': 'ghi',
  '5': 'jkl',
  '6': 'mno',
  '7': 'pqrs',
  '8': 'tuv',
  '9': 'wxyz'
}

  let res = []
  let cur = ''

  const dfs = (i) => {
    if (cur.length === digits.length) {
      res.push(cur)
      return
    }

    for (let c of DIGIT_TO_CHAR[digits[i]]) {
      cur += c
      dfs(i + 1)
      cur = cur.slice(0, -1)
    }
  }

  dfs(0)

  return res
    }
}
