class Node {
    constructor(value) {
        this.value = value
        this.next = null
        this.prev = null
    }
}

class MyDeque {
    constructor() {
        this.dummyHead = new Node(-1)
        this.dummyTail = new Node(-1)

        this.dummyHead.next = this.dummyTail
        this.dummyTail.prev = this.dummyHead
    }

    /**
     * @return {boolean}
     */
    isEmpty() {
        return this.dummyHead.next === this.dummyTail
    }

    /**
     * @param {number} value
     */
    append(value) {
        const newNode = new Node(value)
        newNode.prev = this.dummyTail.prev
        newNode.next = this.dummyTail
        this.dummyTail.prev.next = newNode
        this.dummyTail.prev = newNode
    }

    /**
     * @param {number} value
     * @return {void}
     */
    appendleft(value) {
        const newNode = new Node(value)
        newNode.next = this.dummyHead.next
        newNode.prev = this.dummyHead
        this.dummyHead.next.prev = newNode
        this.dummyHead.next = newNode
    }

    /**
     * @return {number}
     */
    pop() {
        if (this.isEmpty()) {
            return -1
        }
        const targetNode = this.dummyTail.prev
        const value = targetNode.value
        targetNode.prev.next = this.dummyTail
        this.dummyTail.prev = targetNode.prev
        return value
    }

    /**
     * @return {number}
     */
    popleft() {
        if (this.isEmpty()) {
            return -1
        }

        const targetNode = this.dummyHead.next
        const value = targetNode.value
        this.dummyHead.next = targetNode.next
        targetNode.next.prev = this.dummyHead
        return value
    }
}
