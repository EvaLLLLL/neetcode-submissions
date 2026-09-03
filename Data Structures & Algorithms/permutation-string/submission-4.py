class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = Counter(s1)
        s2Freq = defaultdict(int)

        need = len(s1Freq)
        current = 0

        l, r = 0, 0
        while r < len(s2):
            c = s2[r]
            if c not in s1Freq:
                r += 1
                l = r
                current = 0
                s2Freq = defaultdict(int)
                continue

            s2Freq[c] += 1
            if s2Freq[c] == s1Freq[c]:
                current += 1
            
            while s2Freq[c] > s1Freq[c]:
                d = s2[l]
                if s2Freq[d] == s1Freq[d]:
                    current -= 1
                s2Freq[d] -= 1
                l += 1

            if current == need:
                return True
            r += 1

        return False