class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix = nums[i] * prefix

        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * postfix
            postfix = nums[i] * postfix

        return res
