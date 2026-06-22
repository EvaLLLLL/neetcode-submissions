class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keyToValue = defaultdict(list)

        for s in strs:
            key = self.getKey(s)
            keyToValue[key].append(s)

        return list(v for _, v in keyToValue.items()) 

    def getKey(self, s: str) -> List[int]:
        cnt = [0] * 26
        for i in range(len(s)):
            cnt[ord(s[i]) - ord('a')] += 1
        return tuple(cnt)
