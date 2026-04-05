class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let res = 0
        let l = 0
        let r = heights.length - 1

        while (l < r) {
            if (heights[l] < heights[r]) {
                res = Math.max((r - l) * heights[l], res)
                l++
            } else {
                res = Math.max((r - l) * heights[r], res)
                r--
            }
        }

        return res
    }
}
