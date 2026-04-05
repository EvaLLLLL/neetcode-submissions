class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output, subset = [], []
        candidates.sort()

        def backtrack(i, total):
            if total == target:
                output.append(subset[:])
                return
            if i == len(candidates) or total > target:
                return
            
            subset.append(candidates[i])
            backtrack(i + 1, total + candidates[i])

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            subset.pop()
            backtrack(i + 1, total)

        backtrack(0, 0)
        return output
