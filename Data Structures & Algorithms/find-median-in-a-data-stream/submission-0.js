/**
 * const { PriorityQueue, MaxPriorityQueue, MinPriorityQueue } = require('@datastructures-js/priority-queue');
 */
class MedianFinder {
    constructor() {
        // Max Heap for smaller half
        this.small = new PriorityQueue((a, b) => b - a)
        // Min Heap for larger half
        this.large = new PriorityQueue((a, b) => a - b)
    }

    /**
     *
     * @param {number} num
     * @return {void}
     */
    addNum(num) {
        if (this.large.isEmpty() || num >= (this.large.front() || 0)) {
      this.large.enqueue(num)
        } else {
      this.small.enqueue(num)
        }
    
        if (this.small.size() > this.large.size() + 1) {
        this.large.enqueue(this.small.dequeue())
        }
    
        if (this.large.size() > this.small.size() + 1) {
        this.small.enqueue(this.large.dequeue())
        }
    }

    /**
     * @return {number}
     */
    findMedian() {
            if (this.small.size() > this.large.size()) {
      return this.small.front() || 0
    } else if (this.large.size() > this.small.size()) {
      return this.large.front() || 0
    } else {
      return ((this.small.front() || 0) + (this.large.front() || 0)) / 2
    }
    }
}
