class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            cap = (l + r) // 2
            if (self.canShip(cap, days, weights)):
                r = cap - 1
                res = min(res, cap)
            else:
                l = cap + 1
        return res

    def canShip(self, cap: int, days: int, weights: List[int]) -> bool:
        ships, cur = 1, 0

        for w in weights:
            if w > cap:
                return False

            if cur + w > cap:
                ships += 1
                if ships > days:
                    return False
                cur = 0

            cur += w

        return True