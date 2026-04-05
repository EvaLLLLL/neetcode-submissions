class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(n - 1):
            if dp[i] == False:
                return False
                
            k = nums[i]
            while k:
                if i + k > n - 1:
                    k -= 1
                    continue
                dp[i + k] = True
                k -= 1
        
        return dp[n - 1]