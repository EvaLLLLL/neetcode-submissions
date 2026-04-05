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
     * @return {number}
     */
    goodNodes(root) {
        let q = []
        let count = 0

        q.push([root, -Infinity])

        while (q.length) {
            let [node, maxVal] = q.shift()
            
            if (node.val >= maxVal) count++
            if (node.left) q.push([node.left, Math.max(node.val, maxVal)])
            if (node.right) q.push([node.right, Math.max(node.val, maxVal)])
        }

        return count
    }
}
