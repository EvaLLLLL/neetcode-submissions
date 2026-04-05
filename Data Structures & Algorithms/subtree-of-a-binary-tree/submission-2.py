class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSametree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSametree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if (not root1) or (not root2):
            return False
        
        if root1.val != root2.val:
            return False
        
        isLeftSame = self.isSametree(root1.left, root2.left)
        isRightSame = self.isSametree(root1.right, root2.right)
        
        return isLeftSame and isRightSame