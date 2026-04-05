class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsetsWithDup(nums) {
        nums.sort((a, b) => a - b)
        let res = []
        let cur = []

        function backtract(i) {
            if (i >= nums.length) {
                res.push([...cur])
                return
            }

            cur.push(nums[i])
            backtract(i + 1)
            cur.pop()

            while (i + 1 < nums.length && nums[i] === nums[i + 1]) {
                i += 1
            }
            backtract(i + 1)
        }

        backtract(0)
        return res
    }
}
