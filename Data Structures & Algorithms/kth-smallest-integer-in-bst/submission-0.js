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
     * @param {number} k
     * @return {number}
     */
    kthSmallest(root, k) {
        const arr = []
        this.dfs(root, arr, k)
        return arr[k - 1]
    }

    dfs(root, arr, k) {
       if (arr.length === k) return
       if (!root) return

       this.dfs(root.left, arr, k)
       arr.push(root.val)
       this.dfs(root.right, arr, k)
    }
}
