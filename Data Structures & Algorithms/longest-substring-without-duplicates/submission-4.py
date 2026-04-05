class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, l, visit = 0, 0, set()

        for r in range(len(s)):
            while s[r] in visit:
                visit.remove(s[l])
                l += 1
            visit.add(s[r])
            ans = max(ans, r - l + 1)
        return ans