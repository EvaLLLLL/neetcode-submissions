class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.binarySearch(nums, target, True)
        r = self.binarySearch(nums, target, False)
        return [l, r]

    def binarySearch(self, nums: List[int], target: int, isLeft: bool) -> int:
        l, r, i = 0, len(nums) - 1, -1
        
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if isLeft:
                    r = m - 1
                else:
                    l = m + 1
        return i
