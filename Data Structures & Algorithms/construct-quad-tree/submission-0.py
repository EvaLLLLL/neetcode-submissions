"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r, c, side):
            if side == 1:
                return Node(grid[r][c], 1)

            newNode = Node(grid[r][c], 1)

            for row in range(r, r + side):
                for col in range(c, c + side):
                    if grid[row][col] != grid[r][c]:
                        newNode.isLeaf = 0
                        break

            if newNode.isLeaf == 0:
                half = side // 2
                newNode.topLeft = dfs(r, c, half)
                newNode.topRight = dfs(r, c + half, half)
                newNode.bottomLeft = dfs(r + half, c, half)
                newNode.bottomRight = dfs(r + half, c + half, half)
            return newNode

        return dfs(0, 0, len(grid))
