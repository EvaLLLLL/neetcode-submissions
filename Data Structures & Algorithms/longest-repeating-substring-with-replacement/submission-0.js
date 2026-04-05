class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        let left = 0
        let res = 0
        let maxF = 0
        let countMap = new Map()

        for (let right = 0; right < s.length; right++) {
            countMap.set(s[right], (countMap.get(s[right]) || 0) + 1)
            maxF = Math.max(maxF, countMap.get(s[right]) || 0)

            while (right - left + 1 - maxF > k) {
                countMap.set(s[left], (countMap.get(s[left]) || 0) - 1)
                left++
            }

            res = Math.max(res, right - left + 1)
        }

        return res
    }
}
