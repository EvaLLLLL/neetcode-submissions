class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        subset = []

        def backtrack(i, left):
            if left == 0:
                output.append(subset[:])
                return
            if i == len(nums) or left < 0:
                return
            
            subset.append(nums[i])
            backtrack(i, left - nums[i])

            subset.pop()
            backtrack(i + 1, left)

        backtrack(0, target)
        return output