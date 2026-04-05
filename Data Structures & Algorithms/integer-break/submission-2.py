class Solution:
    def integerBreak(self, n: int) -> int:
        ans = 1
        for k in range(2, n + 1):
            x = n // k
            r = n % k
            # Distribute the remainder r across r of the k parts
            # This results in r parts being (x + 1) and (k - r) parts being x
            product = (x + 1)**r * x**(k - r)
            ans = max(ans, product)
        return ans