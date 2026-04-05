class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
  let sum = 0
  let l = 0
  let r = height.length - 1
  let maxL = height[l]
  let maxR = height[r]

  while (l < r) {
    if (maxL <= maxR) {
      sum += maxL - height[l] > 0 ? maxL - height[l] : 0
      l++
      maxL = Math.max(maxL, height[l])
    } else {
      sum += maxR - height[r] > 0 ? maxR - height[r] : 0
      r--
      maxR = Math.max(maxR, height[r])
    }
  }

  return sum
    }
}
