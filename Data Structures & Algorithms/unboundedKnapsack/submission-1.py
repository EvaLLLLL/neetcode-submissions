class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [0] * (M + 1)

        for i in range(N):
            for c in range(1, M + 1):
                skip = dp[c]
                include = 0
                newCap = c - weight[i]
                if newCap >= 0:
                    include = profit[i] + dp[newCap]
                dp[c] = max(skip, include)
        return dp[M]
