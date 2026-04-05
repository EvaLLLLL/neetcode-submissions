class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(left):
            if left in memo:
                return memo[left]

            if left == 0:
                memo[left] = 1
                return memo[left]

            res = 0
            for n in nums:
                if left - n < 0:
                    continue
                res += dfs(left - n)
                
            memo[left] = res
            return res
        
        return dfs(target)
