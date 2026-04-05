class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsets(nums) {
        let res = []
        let curr = []

        function dfs(i) {
            if (i >= nums.length) {
                res.push([...curr])
                return
            }

            curr.push(nums[i])
            dfs(i + 1)

            curr.pop()
            dfs(i + 1)
        }

        dfs(0)
        return res
    }
}
