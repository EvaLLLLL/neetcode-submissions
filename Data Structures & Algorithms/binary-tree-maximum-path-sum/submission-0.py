# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        # return the max value without spliting
        def dfs(root):
            if not root:
                return 0
            
            # dont return the negative
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)

            # compute max path sum WITH spliting at this node
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # return the value without spliting
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]
