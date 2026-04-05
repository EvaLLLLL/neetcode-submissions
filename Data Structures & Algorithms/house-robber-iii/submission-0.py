# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        maxMap = {}

        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0
            if node in maxMap:
                return maxMap[node]

            if node not in maxMap:
                left = node.left
                right = node.right

                rob = node.val + (dfs(left.left) if left else 0) + (dfs(left.right) if left else 0) + (dfs(right.left) if right else 0) + (dfs(right.right) if right else 0)

                norob = (dfs(left) if left else 0) + (dfs(right) if right else 0)

                maxMap[node] = max(rob, norob)
                return maxMap[node]

        dfs(root)
        return maxMap[root]