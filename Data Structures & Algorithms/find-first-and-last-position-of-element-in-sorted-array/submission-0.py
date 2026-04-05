class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        for i in range(len(nums)):
            if nums[i] == target:
                start = min(start, i) if start >= 0 else i
                end = max(end, i) if end >= 0 else i
        return [start, end]