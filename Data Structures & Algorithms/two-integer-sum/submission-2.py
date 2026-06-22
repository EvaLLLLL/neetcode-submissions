class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}

        for i in range(len(nums)):
            left = target - nums[i]
            if left in record:
                return [record[left], i]
            
            record[nums[i]] = i

        return []