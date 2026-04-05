class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @returns {number[][]}
     */
    combinationSum(nums, target) {
        let cur = []
        let res = []

        function backtrack(i, t) {
            if (t === 0) {
                res.push([...cur])
            } else if (t < 0 || i >= nums.length) {
                return
            } else {
                cur.push(nums[i])
                backtrack(i, t - nums[i])

                cur.pop()
                backtrack(i + 1, t)
            }
        }

        backtrack(0, target)

        return res
    }
}
