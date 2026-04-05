class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    permute(nums) {
        let res = []
        let cur = []

        function backtrack(pick) {
            if (cur.length === nums.length) {
                res.push([...cur])
                return
            }

            for (let num of nums) {
                if (!pick[num]) {
                    cur.push(num)
                    pick[num] = true

                    backtrack(pick)
                    
                    cur.pop()
                    pick[num] = false
                }
            }
        }

        backtrack([])

        return res
    }
}
