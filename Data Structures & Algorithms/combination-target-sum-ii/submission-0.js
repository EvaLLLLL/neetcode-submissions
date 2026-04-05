class Solution {
    /**
     * @param {number[]} candidates
     * @param {number} target
     * @return {number[][]}
     */
    combinationSum2(candidates, target) {
        let cur = []
        let res = []

        candidates.sort((a, b) => a - b)

        function backtrack(i, t) {
            if (t === 0) {
                res.push([...cur])
            } else if (t < 0 || i >= candidates.length) {
                return
            } else {
                cur.push(candidates[i])
                backtrack(i + 1, t - candidates[i])

                cur.pop()
                while(i + 1 < candidates.length && candidates[i] === candidates[i+1]) {
                    i++
                }
                backtrack(i + 1, t)
            }
        }

        backtrack(0, target)
        return res
    }
}
