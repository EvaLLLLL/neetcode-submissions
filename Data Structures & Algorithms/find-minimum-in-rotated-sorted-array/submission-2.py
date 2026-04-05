class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]: # left portion
                l = m + 1
            else: # right portion
                r = m
        
        return nums[l]
