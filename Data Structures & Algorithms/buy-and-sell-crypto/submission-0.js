class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
          let l = 0,
    r = 1,
    res = 0

  while (r < prices.length) {
    if (prices[l] >= prices[r]) {
      l = r
    } else {
      res = Math.max(prices[r] - prices[l], res)
    }
    r++
  }

  return res
    }
}
