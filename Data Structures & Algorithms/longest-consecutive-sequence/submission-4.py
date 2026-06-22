class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        indeg = []
        for n in nums:
            if n - 1 not in nums:
                indeg.append(n)

        ans = 0
        for start in indeg:
            length = 1
            while start + 1 in nums:
                length += 1
                start += 1
            ans = max(ans, length)

        return ans
