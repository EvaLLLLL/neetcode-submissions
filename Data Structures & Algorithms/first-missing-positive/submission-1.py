class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mini = min(nums)
        maxi = max(nums)

        if maxi <= 0:
            return 1

        for x in range(1, maxi + 1):
            if x not in nums:
                return x
        return maxi + 1