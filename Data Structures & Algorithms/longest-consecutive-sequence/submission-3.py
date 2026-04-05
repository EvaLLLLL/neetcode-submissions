class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet= set(nums)
        ans = 0
        for x in numSet:
            if x - 1 not in nums:
                length = 1
                while x + length in nums:
                    length += 1
                ans = max(length, ans)
        return ans