class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, cnt = 0, 0

        for num in nums:
            if cnt == 0:
                res = num
            cnt += (1 if num == res else -1)
        return res