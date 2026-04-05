class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = { 0: 1 }
        cur, res = 0, 0

        for x in nums:
            cur += x
            diff = cur - k

            res += prefix.get(diff, 0)
            prefix[cur] = 1 + prefix.get(cur, 0)
        
        return res