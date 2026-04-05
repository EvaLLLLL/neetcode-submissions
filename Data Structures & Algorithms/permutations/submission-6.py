class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, perm = [], []
        picked = [False] * len(nums)

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm[:])
                return

            for i in range(len(nums)):
                if not picked[i]:
                    perm.append(nums[i])
                    picked[i] = True
                    backtrack()

                    perm.pop()
                    picked[i] = False
        
        backtrack()
        return res