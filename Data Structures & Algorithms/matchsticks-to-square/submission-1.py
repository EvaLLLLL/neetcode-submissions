class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        side = [0] * 4
        target = sum(matchsticks) // 4
        n = len(matchsticks)

        matchsticks.sort(reverse=True)

        if matchsticks[0] > target:
            return False

        def backtrack(index):
            if index == n:
                return True

            for i in range(4):
                if side[i] + matchsticks[index] <= target:
                    side[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    side[i] -= matchsticks[index]

            return False

        return backtrack(0)
