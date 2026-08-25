class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map = {val: i for i, val in enumerate(inorder)}
        def build(p_start, p_end, i_start, i_end):
            if p_start > p_end:
                return None
            
            rootVal = preorder[p_start]
            rootIndex = in_map[rootVal]
            leftSize = rootIndex - i_start
            
            root = TreeNode(rootVal)
            root.left = build(p_start + 1, p_start + leftSize, i_start, rootIndex - 1)
            root.right = build(p_start + leftSize + 1, p_end, rootIndex + 1, i_end)
            return root
            
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)