class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ans = -1

        for a, b in trust:
            if ans != -1 and (b != ans or a == ans):
                return -1
            ans = b
        
        return ans
            