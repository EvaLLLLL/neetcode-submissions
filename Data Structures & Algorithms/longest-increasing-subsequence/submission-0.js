class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    lengthOfLIS(nums) {
        const len = nums.length
        const LTS = new Array(len).fill(1)

        for (let i = len - 1; i >= 0; i--) {
            for (let j = i + 1; j < len; j++) {
                if (nums[i] < nums[j]) {
                    LTS[i] = Math.max(LTS[i], 1 + LTS[j])
                }
            }
        }

        return Math.max(...LTS)
    }
}
