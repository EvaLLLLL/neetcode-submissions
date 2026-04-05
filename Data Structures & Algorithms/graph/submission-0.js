class Graph {
    constructor() {
        this.adjList = new Map()
    }

    /**
     * @param {number} src
     * @param {number} dst
     * @return {void}
     */
    addEdge(src, dst) {
        if (!this.adjList.has(src)) {
            this.adjList.set(src, new Set())
        }
        if (!this.adjList.has(dst)) {
            this.adjList.set(dst, new Set())
        }
        this.adjList.set(src, this.adjList.get(src).add(dst))
    }

    /**
     * @param {number} src
     * @param {number} dst
     * @return {boolean}
     */
    removeEdge(src, dst) {
        if (this.adjList.has(src) && this.adjList.has(dst)) {
            this.adjList.get(src).delete(dst)
            return true
        }
        return false
    }

    /**
     * @param {number} src
     * @param {number} dst
     * @return {boolean}
     */
    hasPath(src, dst) {
        const visited = new Set()

        const dfs = (f, t) => {
            if (f === t) return true

            visited.add(f)

            if (this.adjList.has(f)) {
                for (let n of this.adjList.get(f) || []) {
                    if (!visited.has(n) && dfs(n, dst)) {
                        return true
                    }
                }
            }

            return false
        }

        return dfs(src, dst)
    }
}
