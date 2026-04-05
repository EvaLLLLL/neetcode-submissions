class Solution {
    /**
     * @param {character[]} tasks
     * @param {number} n
     * @return {number}
     */
    leastInterval(tasks, n) {
        let count = new Array(26).fill(0)

        for (let t of tasks) {
            count[t.charCodeAt(0) - 'A'.charCodeAt(0)]++
        }

        let maxHeap = new MaxPriorityQueue()
        for (let i = 0; i < 26; i++) {
            if (count[i] > 0) maxHeap.push(count[i])
        }

        let time = 0
        let q = []

        while (maxHeap.size() > 0 || q.length > 0) {
            time++

            if (maxHeap.size() > 0) {
                let cnt = maxHeap.pop() - 1
                if (cnt > 0) {
                    q.push([cnt, time + n])
                }
            }

            if (q.length > 0 && q[0][1] === time) {
                maxHeap.push(q.shift()[0])
            }
        }

        return time
    }
}
