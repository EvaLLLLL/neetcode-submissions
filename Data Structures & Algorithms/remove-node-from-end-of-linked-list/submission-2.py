# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        p1Prev, p1, p2 = dummy, head, head

        while n > 1:
            p2 = p2.next
            n -= 1

        while p2.next:
            p1 = p1.next
            p2 = p2.next
            p1Prev = p1Prev.next

        p1Prev.next = p1.next
        return dummy.next
