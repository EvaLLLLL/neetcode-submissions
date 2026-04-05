/**
* const { MaxPriorityQueue } = require("@datastructures-js/priority-queue")
*/
class Twitter {
    constructor() {
        this.time = 0
        this.tweetMap = new Map()
        this.followMap = new Map()
    }

    /**
     * @param {number} userId
     * @param {number} tweetId
     * @return {void}
     */
    postTweet(userId, tweetId) {
        if (!this.tweetMap.has(userId)) this.tweetMap.set(userId, []);
        this.tweetMap.get(userId).push([this.time++, tweetId]);
    }

    /**
     * @param {number} userId
     * @return {number[]}
     */
    getNewsFeed(userId) {
        if (!this.followMap.has(userId)) {
            this.followMap.set(userId, new Set())
        }
        this.followMap.get(userId).add(userId)
        const maxHeap = new MaxPriorityQueue(v => v[0])

        for (const followeeId of this.followMap.get(userId)) {
            if (this.tweetMap.has(followeeId)) {
                const tweets = this.tweetMap.get(followeeId)
                const index = tweets.length - 1
                const [time, tweetId] = tweets[index]
                maxHeap.enqueue([time, tweetId, followeeId, index - 1])
            }
        }

        let res = []
        while (!maxHeap.isEmpty() && res.length < 10) {
            const [_, tweetId, followeeId, nextIndex] = maxHeap.dequeue()
            res.push(tweetId)

            if (nextIndex >= 0) {
                const [olderTime, olderTweetId] = this.tweetMap.get(followeeId)[nextIndex]
                maxHeap.enqueue([olderTime, olderTweetId, followeeId, nextIndex - 1])
            }
        }

        return res
    }

    /**
     * @param {number} followerId
     * @param {number} followeeId
     * @return {void}
     */
    follow(followerId, followeeId) {
        if (followerId !== followeeId) {
            if (!this.followMap.has(followerId)) {
                this.followMap.set(followerId, new Set())
            }
            this.followMap.get(followerId).add(followeeId)
        }
    }

    /**
     * @param {number} followerId
     * @param {number} followeeId
     * @return {void}
     */
    unfollow(followerId, followeeId) {
        if (this.followMap.has(followerId)) {
            this.followMap.get(followerId).delete(followeeId)
        }
    }
}
