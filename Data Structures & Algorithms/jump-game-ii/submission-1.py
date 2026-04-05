class Solution:
    def jump(self, nums: List[int]) -> int:
        res, l, r = 0, 0, 0

        while r < len(nums) - 1:
            maxPos = 0
            for i in range(l, r + 1):
                maxPos = max(maxPos, nums[i] + i)
            
            l = r + 1
            r = maxPos
            res += 1
        return res