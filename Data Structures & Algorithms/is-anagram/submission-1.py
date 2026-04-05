class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = Counter(s)
        for c in t:
            if c not in cnt or not cnt[c]:
                return False
            cnt[c] = cnt[c] - 1
        return all(count == 0 for count in cnt.values())