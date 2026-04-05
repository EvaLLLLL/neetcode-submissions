class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    findKthLargest(nums, k) {
        const idx = nums.length - k
        function quickSelect(s, e) {
            let p = s

            for (let i = s; i < e; i++) {
                if (nums[i] <= nums[e]) {
                    [nums[p], nums[i]] = [nums[i], nums[p]]
                    p++
                }
            }

            [nums[p], nums[e]] = [nums[e], nums[p]]

            if (p > idx) {
                return quickSelect(s, p - 1)
            } else if (p < idx) {
                return quickSelect(p + 1, e)
            } else {
                return nums[p]
            }
        }

        return quickSelect(0, nums.length - 1)
    }
}
