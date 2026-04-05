class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        cur = head
        while cur:
            nxt = cur.next
            if cur.val != val:
                tail.next = cur
                cur.next = None
                tail = cur
            cur = nxt
        return dummy.next