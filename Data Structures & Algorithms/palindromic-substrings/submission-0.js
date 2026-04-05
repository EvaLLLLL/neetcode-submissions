class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    countSubstrings(s) {
        let count = 0

        for (let i = 0; i < s.length; i++) {
            count += this.countPali(s, i, i)            
            count += this.countPali(s, i, i + 1)
        }

        return count
    }

    countPali(s, l, r) {
        let count = 0

        while (l >= 0 && r < s.length && s[l] === s[r]) {
            count++
            l--
            r++
        }

        return count
    }
}
