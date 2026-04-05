class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[i][1] allow to buy
        # dp[i][0] not allow to buy
        dp = [[0, 0] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            # allow to buy
            buy = dp[i + 1][0] - prices[i] if i + 1 < n else -prices[i]
            cooldown = dp[i + 1][1] if i + 1 < n else 0
            dp[i][1] = max(buy, cooldown)

            # not allow to buy
            sell = dp[i + 2][1] + prices[i] if i + 2 < n else prices[i]
            cooldown = dp[i + 1][0] if i + 1 < n else 0
            dp[i][0] = max(sell, cooldown)
        
        return dp[0][1]