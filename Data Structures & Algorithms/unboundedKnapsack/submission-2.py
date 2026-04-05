class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [0] * (M + 1)

        for i in range(N):
            for c in range(weight[i], M + 1):
                dp[c] = max(dp[c], profit[i] + dp[c - weight[i]])
        return dp[M]
