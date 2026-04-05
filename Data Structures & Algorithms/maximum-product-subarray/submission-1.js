class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxProduct(nums) {
          let currMax = 1
  let currMin = 1
  let res = nums[0]

  for (let num of nums) {
    const tmp = num * currMax
    currMax = Math.max(num * currMax, num * currMin, num)
    currMin = Math.min(tmp, num * currMin, num)
    res = Math.max(res, currMax)
  }

  return res
    }
}
