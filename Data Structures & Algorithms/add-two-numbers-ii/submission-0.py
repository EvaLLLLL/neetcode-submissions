# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        l1, l2 = self._reverse(l1), self._reverse(l2)
        l3 = self._add(l1, l2)
        return self._reverse(l3)
    
    def _reverse(self, l: ListNode | None) -> ListNode | None:
        if not l or not l.next:
            return l

        head = self._reverse(l.next)
        l.next.next = l
        l.next = None
        return head

    def _add(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1)
        cur = dummy
        p1, p2 = l1, l2

        carry = 0
        while p1 or p2 or carry > 0:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0

            value = v1 + v2 + carry
            v = value % 10
            carry = value // 10
            cur.next = ListNode(v)

            cur = cur.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        return dummy.next
