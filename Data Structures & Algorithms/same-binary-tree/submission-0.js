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
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {boolean}
     */
    isSameTree(p, q) {
  if (!p && !q) return true

  if (p?.val !== q?.val) return false

  if (!this.isSameTree(p?.left || null, q?.left || null)) return false
  if (!this.isSameTree(p?.right || null, q?.right || null)) return false

  return true
    }
}
