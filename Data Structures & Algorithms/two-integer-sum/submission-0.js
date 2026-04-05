class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = new Map()

        for (let i=0; i < nums.length; i++) {
            const flag = map.get(nums[i])
            if (flag !== undefined) {
                return [i, flag]
            }

            map.set(target - nums[i], i)
        }

        return []
    }
}
