class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm, used):
            if len(perm) == len(nums):
                res.append(perm[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                perm.append(nums[i])
                backtrack(perm, used)
                perm.pop()
                used[i] = False
        
        backtrack([], [False] * len(nums))
        return res