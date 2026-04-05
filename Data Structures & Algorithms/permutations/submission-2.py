class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i: int, cur: List[int]):
            if len(cur) == len(nums):
                res.append(cur[:])
                return

            for x in nums:
                if x not in cur:
                    cur.append(x)
                    backtrack(i + 1, cur)
                    cur.pop()

        backtrack(0, [])
        return res