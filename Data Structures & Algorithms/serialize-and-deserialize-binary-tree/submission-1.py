# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        if root is None:
            return "#"
        
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return f"{left},{right},{root.val}"
        

    def deserialize(self, data):
        nodes = data.split(",")
        return self._deserialize(nodes)
    
    def _deserialize(self, nodes):
        if not nodes:
            return None

        rootVal = nodes.pop()
        if not rootVal or rootVal == "#":
            return None

        root = TreeNode(int(rootVal))
        root.right = self._deserialize(nodes)
        root.left = self._deserialize(nodes)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))