# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # ... --> prevNode --> subListHead --> ... --> subListTail --> nextNode --> ...

        dummy = ListNode(0)
        dummy.next = head

        prevNode = dummy
        for _ in range(left - 1):
            prevNode = prevNode.next

        subListHead = prevNode.next
        subListTail = subListHead
        for _ in range(right - left):
            subListTail = subListTail.next

        nextNode = subListTail.next
        subListTail.next = None
        reversedSubList = self.reverse(subListHead)
        prevNode.next = reversedSubList
        subListHead.next = nextNode

        return dummy.next

    def reverse(self, head):
        if not head:
            return head

        newHead = head
        if head.next:
            newHead = self.reverse(head.next)
            head.next.next = head
        head.next = None
        return newHead
