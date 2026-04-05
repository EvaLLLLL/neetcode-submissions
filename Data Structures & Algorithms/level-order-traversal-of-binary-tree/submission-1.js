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
     * @return {number[][]}
     */
    levelOrder(root) {
        let res = []
        let queue = []

        if (root) queue.push(root)

        while (queue.length) {
           let level = []
           for (let i = queue.length; i > 0; i--) {
           
            const node = queue.shift()

            if (node.left) queue.push(node.left)
            if (node.right) queue.push(node.right)

            level.push(node.val)
           } 
           res.push(level)
        }

        return res
    }
}
