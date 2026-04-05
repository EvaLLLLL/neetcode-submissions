class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans, left, count_zeros = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count_zeros += 1

            while count_zeros > k:
                if nums[left] == 0:
                    count_zeros -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
