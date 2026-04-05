class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = new Map()

        for (const str of strs) {
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
