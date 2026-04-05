/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    addTwoNumbers(l1, l2) {
          const dummy = new ListNode(0)
  let cur = dummy
  let carry = 0

  while (l1 || l2 || carry) {
    const val = (l1?.val || 0) + (l2?.val || 0) + carry
    cur.next = new ListNode(val % 10)
    carry = Math.floor(val / 10)

    cur = cur.next
    l1 = l1?.next ?? null
    l2 = l2?.next ?? null
  }

  return dummy.next
    }
}
