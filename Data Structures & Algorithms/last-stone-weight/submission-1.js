/**
 * const { MaxPriorityQueue } = require('@datastructures-js/priority-queue');
 */

class Solution {
    /**
     * @param {number[]} stones
     * @return {number}
     */
    lastStoneWeight(stones) {
        const maxHeap = new MaxPriorityQueue()

        for (let num of stones) {
            maxHeap.enqueue(num)
        }

        while (maxHeap.size() > 1) {
            let x = maxHeap.dequeue()
            let y = maxHeap.dequeue()
            maxHeap.enqueue(Math.abs(x - y))
        }

        return maxHeap.size() === 1 ? maxHeap.dequeue() : 0
    }
}
