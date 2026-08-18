# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        index = 0
        for head in lists:
            while head:
                tmp = head.next
                head.next = None
                heapq.heappush(minHeap, (head.val, index, head))
                head = tmp
                index += 1

        dummy = ListNode(-1)
        p = dummy
        while minHeap:
            val, index, node = heapq.heappop(minHeap)
            p.next = node
            p = p.next

        return dummy.next