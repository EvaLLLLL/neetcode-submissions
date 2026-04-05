class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freqMap = nums.reduce((pre, curr) => {
            if (pre[curr] !== undefined) {
                pre[curr]++
            } else {
                pre[curr] = 1
            }
            return pre
        }, {})

        const freqs = Object.values(freqMap).sort((a, b) => b - a).filter((_, index) => index < k)

        const result = nums.reduce((pre, curr) => {
            if (!pre.includes(curr) && freqs.includes(freqMap[curr])) {
                pre.push(curr)
            }
            return pre
        }, [])

        return result
    }
}
