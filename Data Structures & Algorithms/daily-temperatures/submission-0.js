class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        let output = Array(temperatures.length).fill(0)
        let stack = []

        for (let i = 0; i < temperatures.length; i++) {
            const t = temperatures[i]

            while (stack.length && t > stack[stack.length - 1][0]) {
                const [_, stackIdx] = stack.pop()
                output[stackIdx] = i - stackIdx
            }

            stack.push([t, i])
        }

        return output
    }
}
