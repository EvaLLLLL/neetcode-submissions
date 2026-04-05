class Solution {
    /**
     * @param {string} s
     * @return {string}
     */
    longestPalindrome(s) {
        let resIndex = 0
        let resLen = 0

        for (let i = 0; i < s.length; i++) {
            let l = i
            let r = i

            while (l >= 0 && r < s.length && s[l] === s[r]) {
                if (r - l + 1 > resLen) {
                    resLen = r - l + 1
                    resIndex = l
                }
                l--
                r++
            }

            l = i
            r = i + 1

            while (l >= 0 && r < s.length && s[l] === s[r]) {
                if (r - l + 1 > resLen) {
                    resLen = r - l + 1
                    resIndex = l
                }
                l--
                r++
            }
        }

        return s.substring(resIndex, resIndex + resLen)
    }
}
