class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = defaultdict(int)
        
        def dfs(s: int, e: int, total: int) -> int:
            if (s, e) in cache:
                return cache.get((s, e))

            if s > e:
                cache[(s, e)] = total
                return total

            even = (s - e) % 2 == 0
            left = piles[s] if even else 0
            right = piles[e] if even else 0
            first = dfs(s + 1, e, left + total)
            last = dfs(s, e - 1, right + total)
            total = max(first, last)
            cache[(s, e)] = total
            return total

        alice = dfs(0, len(piles) - 1, 0)
        return 2 * alice > sum(piles)