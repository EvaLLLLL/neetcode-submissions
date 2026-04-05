class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        l = 0
        for r in range(n - 1, -1, -1):
            if r <= l:
                return

            s[l], s[r] = s[r], s[l]
            l += 1
