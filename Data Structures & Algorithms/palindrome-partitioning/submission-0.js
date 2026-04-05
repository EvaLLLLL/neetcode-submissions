class Solution {
    /**
     * @param {string} s
     * @return {string[][]}
     */
    partition(s) {
        let res = []
        let cur = []

        const dfs = (i) => {
            if (i >= s.length) {
                res.push([...cur])
                return
            }

            for (let j = i; j < s.length; j++) {
                const str = s.substring(i, j+1)
                if (this.isPali(str)) {
                    cur.push(str)
                    dfs(j + 1)
                    cur.pop()
                }
            }
        }

        dfs(0)
        return res
    }

    /**
     * @param {string} str
     * @return {boolean}
     */
    isPali(str) {
        let l = 0
        let r = str.length - 1

        while (l < r) {
            if (str[l] !== str[r]) return false
            l++
            r--
        }

        return true
    }
}
