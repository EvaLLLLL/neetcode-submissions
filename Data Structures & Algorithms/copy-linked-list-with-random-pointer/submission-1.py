"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cache = {}

        def copy(node):
            if not node:
                return None

            if node in cache:
                return cache[node]

            newNode = Node(node.val)
            cache[node] = newNode
            newNode.next = copy(node.next)
            newNode.random = copy(node.random)
            return newNode

        return copy(head) 
