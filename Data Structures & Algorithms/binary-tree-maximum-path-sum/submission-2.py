
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 0

            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            ans = max(ans, node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return ans