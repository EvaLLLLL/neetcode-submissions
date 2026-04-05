/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number[]}
     */
    rightSideView(root) {
        let res = []
        let queue = []

        if (root) queue.push(root)

        while (queue.length) {
            let rightSide = null
            let qlen = queue.length

            for (let i = 0; i < qlen; i++) {
                let node = queue.shift()

                if (node) {
                    rightSide = node
                    queue.push(node.left)
                    queue.push(node.right)
                }
            }

            if (rightSide) {
                res.push(rightSide.val)
            }
        }

        return res
    }
}
