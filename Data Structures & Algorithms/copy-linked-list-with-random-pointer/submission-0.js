// class Node {
//   constructor(val, next = null, random = null) {
//       this.val = val;
//       this.next = next;
//       this.random = random;
//   }
// }

class Solution {
    /**
     * @param {Node} head
     * @return {Node}
     */
    copyRandomList(head) {
        if (!head) return null

        let copied = new Map()

        const copy = (node) => {
            if (!node) return null

            if (copied.has(node)) {
                return copied.get(node)
            }

            const newNode = new Node(node.val)
            copied.set(node, newNode)

            newNode.next = copy(node.next)
            newNode.random = copy(node.random)
            
            return newNode
        }

        return copy(head)
    }
}
