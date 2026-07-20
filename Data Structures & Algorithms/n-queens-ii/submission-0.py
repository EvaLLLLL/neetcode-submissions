class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDiag = set()
        negDiag = set()
        ans = 0

        def backtrack(r):
            nonlocal ans
            if r == n:
                ans += 1
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                backtrack(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return ans
