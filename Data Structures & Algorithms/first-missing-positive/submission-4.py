class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(n):
            idx = abs(nums[i]) - 1 
            if idx < 0 or idx >= len(nums):
                continue
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
            elif nums[idx] == 0:
                nums[idx] = -(n + 1)

        for i in range(1, n + 1):
            idx = i - 1
            if nums[idx] >= 0:
                return i
        
        return n + 1
