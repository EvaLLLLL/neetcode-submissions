class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = self.binaryExp(x, abs(n))
        return ans if n >= 0 else 1/ans
    
    def binaryExp(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        ans = self.binaryExp(x * x, n // 2)
        if n % 2:
            ans = x * ans

        return ans