class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols, posDiag, negDiag = set(), set(), set()

        def backtrack(r: int, cur: List[str]):
            if r >= n:
                res.append(cur[:])
                return

            for c in range(n):
                if (c in cols) or ((r - c) in posDiag) or ((r + c) in negDiag):
                    continue

                cols.add(c)
                negDiag.add(r + c)
                posDiag.add(r - c)
                cur.append("." * c + "Q" + (n - c - 1) * ".")
                backtrack(r + 1, cur)

                cur.pop()
                cols.remove(c)
                negDiag.remove(r + c)
                posDiag.remove(r - c)

        backtrack(0, [])
        return res
