# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.add(l1, l2, 0)

    def add(self, node1: Optional[ListNode], node2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        if not node1 and not node2 and carry == 0:
            return None

        v1 = node1.val if node1 else 0
        v2 = node2.val if node2 else 0

        new_carry, val = divmod(v1 + v2 + carry, 10)

        next_node = self.add(node1.next if node1 else None, node2.next if node2 else None, new_carry)

        return ListNode(val, next_node)

