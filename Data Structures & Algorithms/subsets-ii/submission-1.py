class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i: int, cur: List[int]):
            if i >= len(nums):
                res.append(cur[:])
                return

            cur.append(nums[i])
            backtrack(i + 1, cur)
            cur.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, cur)

        backtrack(0, [])
        return res