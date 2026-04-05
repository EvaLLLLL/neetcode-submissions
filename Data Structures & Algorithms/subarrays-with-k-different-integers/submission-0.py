class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k - 1)
        
    def atMost(self, nums, k):
        count = collections.Counter()
        l = 0
        res = 0
        for r in range(len(nums)):
            if count[nums[r]] == 0:
                k -= 1
            count[nums[r]] += 1

            while k < 0:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    k += 1
                l += 1
            res += r - l + 1
        return res
