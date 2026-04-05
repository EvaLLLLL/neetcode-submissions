class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        subset = []

        def backtrack(totalLen):
            if totalLen == len(s):
                string = "".join(subset)
                if string == s:
                    res.append(" ".join(subset))
                return

            for w in wordDict:
                if len(w) + totalLen <= len(s):
                    subset.append(w)
                    backtrack(totalLen + len(w))
                    subset.pop()
        
        backtrack(0)
        return res
