class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs[0])
        res = ""

        for i in range(n):
            cur = strs[0][:i+1]
            for s in strs:
                if not s.startswith(cur):
                    return res
            res += strs[0][i]
        return res