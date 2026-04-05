class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [0]
        for wgt in w:
            self.prefix.append(self.prefix[-1] + wgt)

    def pickIndex(self) -> int:
        target = self.prefix[-1] * random.random()
        l, r = 1, len(self.prefix)

        while l < r:
            m = (l + r) // 2
            if self.prefix[m] <= target:
                l = m + 1
            else:
                r = m
        return l - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()