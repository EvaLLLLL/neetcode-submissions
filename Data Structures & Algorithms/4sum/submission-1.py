class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.kSum(nums, target, 4)

    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(i):
            if len(subset) == k:
                if sum(subset) == target:
                    res.append(subset[:])
                return

            if i >= len(nums):
                return

            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1

            dfs(i + 1)
        
        dfs(0)
        return res