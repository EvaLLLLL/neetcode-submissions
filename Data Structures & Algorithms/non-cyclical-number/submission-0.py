class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.squareOfNum(n)

        while slow != fast:
            slow = self.squareOfNum(slow)
            fast = self.squareOfNum(fast)
            fast = self.squareOfNum(fast)
        return True if fast == 1 else False
        

    def squareOfNum(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            output += digit ** 2 
            n = n // 10
        return output
        