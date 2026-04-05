class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
  let l = 0
  let r = Math.max(...piles)
  let result = r

  while (l <= r) {
    const k = Math.floor((l + r) / 2)
    const minH = piles.reduce((pre, curr) => (pre += Math.ceil(curr / k)), 0)

    if (minH <= h) {
      result = k
      r = k - 1
    } else {
      l = k + 1
    }
  }

  return result

    }
}
