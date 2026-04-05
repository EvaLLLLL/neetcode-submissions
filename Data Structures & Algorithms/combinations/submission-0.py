class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, subset = [], []

        def backtrack(i: int):
            if len(subset) == k:
                res.append(subset[:])
                return
            if i > n:
                return

            subset.append(i)
            backtrack(i + 1)

            subset.pop()
            backtrack(i + 1)

        backtrack(1)
        return res