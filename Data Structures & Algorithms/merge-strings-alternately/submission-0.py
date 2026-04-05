class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        p1, p2 = 0, 0

        ans = ""
        while p1 < n1 and p2 < n2:
            if len(ans) % 2 == 0:
                ans += word1[p1]
                p1 += 1
            else:
                ans += word2[p2]
                p2 += 1
        
        if p1 < n1:
            ans += word1[p1:]
        if p2 < n2:
            ans += word2[p2:]
        return ans
        