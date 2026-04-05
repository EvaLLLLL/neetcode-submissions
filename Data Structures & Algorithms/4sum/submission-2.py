class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []
        
        def kSum(start, target, k):
            if k == 2:
                l, r = start, len(nums) - 1

                while l < r:
                    cur = nums[l] + nums[r]
                    if cur > target:
                        r -= 1
                    elif cur < target:
                        l += 1
                    else:
                        res.append(quad + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                return

            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                kSum(i + 1, target - nums[i], k - 1)
                quad.pop()

        kSum(0, target, 4)
        return res
