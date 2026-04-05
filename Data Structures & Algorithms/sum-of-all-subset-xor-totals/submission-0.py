class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0

        def backtrack(i: int, cur: List[int]):
            nonlocal total
            xorr = 0
            if i >= len(nums):
                for x in cur:
                    xorr ^= x
                total += xorr
                return

            cur.append(nums[i])
            backtrack(i + 1, cur)
            cur.pop()
            backtrack(i + 1, cur)
        
        backtrack(0, [])
        return total