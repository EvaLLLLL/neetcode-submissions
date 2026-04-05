class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = new Map()

        for (let i = 0; i < strs.length; i++) {
            const str = strs[i]
            const sortedStr = str.split('').sort().join('')
            const arr = map.get(sortedStr)
            if (Array.isArray(arr)) {
                map.set(sortedStr, [...arr, str])
            } else {
                map.set(sortedStr, [str])
            }
        }

        return [...map.values()]
    }
}
