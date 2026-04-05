class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        res = []
        carry = 0
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                v = digits[i] + 1
            else:
                v = digits[i] + carry

            carry = v // 10
            res.append(v % 10)
        if carry:
            res.append(carry)

        return res[::-1]
