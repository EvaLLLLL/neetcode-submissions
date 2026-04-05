class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        l, r = 1, n - 2
        peak = -1

        while l <= r:
            m = (l + r) // 2
            left_val = mountainArr.get(m - 1)
            mid_val = mountainArr.get(m)
            right_val = mountainArr.get(m + 1)

            if left_val < mid_val < right_val:
                l = m + 1
            elif left_val > mid_val > right_val:
                r = m - 1
            else:
                peak = m
                break

        peak_val = mountainArr.get(peak)
        if target == peak_val:
            return peak

        # left portion
        l, r = 0, peak - 1
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m

        # right portion
        l, r = peak + 1, n - 1
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)
            if val < target:
                r = m - 1
            elif val > target:
                l = m + 1
            else:
                return m

        return -1
