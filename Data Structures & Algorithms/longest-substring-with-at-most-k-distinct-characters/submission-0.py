class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        chars = {} # { c: count }

        for r in range(len(s)):
            chars[s[r]] = 1 + chars.get(s[r], 0)

            if len(chars) > k:
                chars[s[l]] -= 1
                if chars[s[l]] == 0:
                    del chars[s[l]]
                l += 1

            ans = max(ans, r - l + 1)
        return ans