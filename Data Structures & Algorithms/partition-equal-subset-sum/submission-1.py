class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) / 2
        dp = set()

        dp.add(0)
        dp.add(nums[0])

        for i in range(1, len(nums)):
            for s in dp.copy():
                if target in dp:
                    return True

                dp.add(s + nums[i])

        return False
            