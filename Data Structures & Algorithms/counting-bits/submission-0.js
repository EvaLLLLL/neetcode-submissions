class Solution {
    /**
     * @param {number} n
     * @return {number[]}
     */
    countBits(n) {
          const output = new Array(n + 1).fill(0)

  for (let i = 1; i <= n; i++) {
    let count = 0
    let num = i
    while (num) {
      if ((num & 1) === 1) count++
      num >>= 1
    }
    output[i] = count
  }

  return output
    }
}
