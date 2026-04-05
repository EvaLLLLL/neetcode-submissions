"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cache = {} # old: new
        def copy(root):
            if not root:
                return None
            if root in cache:
                return cache[root]
            
            newNode = Node(root.val)
            cache[root] = newNode
            newNode.neighbors = [copy(nei) for nei in root.neighbors]
            return newNode
        return copy(node)