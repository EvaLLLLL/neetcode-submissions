class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(i):
            if len(subset) == 4:
                if sum(subset) == target:
                    res.append(subset[:])
                return

            if i >= len(nums):
                return

            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            # Decision NOT to include nums[i]
            # Skip duplicates to avoid duplicate quadruplets
            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1

            dfs(i + 1)
        
        dfs(0)
        return res