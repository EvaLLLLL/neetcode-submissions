/**
 * const { MinPriorityQueue } = require('@datastructures-js/priority-queue');
 */
class Solution {
    /**
     * @param {number[][]} points
     * @param {number} k
     * @return {number[][]}
     */
    kClosest(points, k) {
          const minHP = new MinPriorityQueue(
    ([x, y]) => x ** 2 + y ** 2
  )

  for (let [x, y] of points) {
    minHP.enqueue([x, y])
  }

  let res = []
  for (let i = 0; i < k; i++) {
    res.push(minHP.dequeue())
  }

  return res
    }
}
