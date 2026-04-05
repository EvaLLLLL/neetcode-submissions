class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0, 0, 0]
        for x in nums:
            cnt[x] += 1
        
        index = 0
        for i in range(3):
            while cnt[i]:
                cnt[i] -= 1
                nums[index] = i
                index += 1