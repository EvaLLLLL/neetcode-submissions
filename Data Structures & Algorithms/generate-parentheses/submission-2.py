class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, subset = [], []

        def backtrack(closedN, openN):
            if closedN == openN == n:
                res.append("".join(subset))
                return

            if closedN < openN:
                subset.append(")")
                backtrack(closedN + 1, openN)
                subset.pop()
            
            if openN < n:
                subset.append("(")
                backtrack(closedN, openN + 1)
                subset.pop()

        backtrack(0, 0)
        return res