class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in idx:
                return [idx[diff], i]
            idx[nums[i]] = i
        return []