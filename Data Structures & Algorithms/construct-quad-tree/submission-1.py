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

            half = side // 2
            topLeft = dfs(r, c, half)
            topRight = dfs(r, c + half, half)
            bottomLeft = dfs(r + half, c, half)
            bottomRight = dfs(r + half, c + half, half)

            if (
                topLeft.isLeaf and
                topRight.isLeaf and
                bottomLeft.isLeaf and
                bottomRight.isLeaf and
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val
            ):
                return Node(topLeft.val, 1)

            return Node(topLeft.val, 0, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(0, 0, len(grid))
