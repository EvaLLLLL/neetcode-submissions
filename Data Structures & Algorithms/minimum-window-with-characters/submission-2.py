class Solution:
    def minWindow(self, s: str, t: str) -> str:
        candidates = []

        for i in range(len(s)):
            if s[i] in t:
                candidates.append(i)

        tCount = Counter(t)
        target = len(tCount.keys())
        ans = ""

        for l in candidates:
            sCount = Counter(s[l])
            current = 1 if sCount[s[l]] == tCount[s[l]] else 0

            for r in range(l, len(s)):
                if r > l and s[r] in t:
                    sCount[s[r]] = sCount.get(s[r], 0) + 1
                    if sCount[s[r]] == tCount[s[r]]:
                        current += 1

                if current == target:
                    if ans == "" or r - l + 1 < len(ans):
                        ans = s[l:r+1]
                    break

        return ans
