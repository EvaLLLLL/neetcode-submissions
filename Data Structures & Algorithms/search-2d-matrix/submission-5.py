class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r, col = 0, ROWS - 1, -1
        while l <= r:
            m = (l + r) // 2
            row = matrix[m]
            if target > row[-1]:
                l = m + 1
            elif target < row[0]:
                r = m - 1
            else:
                col = m
                break

        if col == -1:
            return False

        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[col][m]:
                l = m + 1
            elif target < matrix[col][m]:
                r = m - 1
            else:
                return True
        
        return False