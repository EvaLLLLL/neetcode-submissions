class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        current_sum = {0: 1}

        for num in nums:
            next_sum = defaultdict(int)
            for s, count in current_sum.items():
                next_sum[s + num] += count
                next_sum[s - num] += count
            current_sum = next_sum

        return current_sum[target] if target in current_sum else 0
