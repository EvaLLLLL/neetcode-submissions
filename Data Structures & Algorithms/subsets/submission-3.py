class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub, res = [], []
    
        def backtrack(start: int) -> None:
            res.append(sub[:])

            for i in range(start, len(nums)):
                sub.append(nums[i])
                backtrack(i + 1)
                sub.pop()
        
        backtrack(0)
        return res