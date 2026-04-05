class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if (r in rows) or (c in cols):
                    matrix[r][c] = 0
        