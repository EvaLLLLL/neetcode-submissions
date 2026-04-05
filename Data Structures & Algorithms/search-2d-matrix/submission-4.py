class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for c in matrix:
            l, r = 0, len(c) - 1

            while l <= r:
                m = (l + r) // 2
                if target > c[m]:
                    l = m + 1
                elif target < c[m]:
                    r = m - 1
                else:
                    return True

        return False 