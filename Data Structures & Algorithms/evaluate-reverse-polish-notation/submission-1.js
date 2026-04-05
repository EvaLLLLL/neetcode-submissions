class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        const stack = []

        for (const t of tokens) {
            switch (t) {
                case "+":
                    stack.push(stack.pop() + stack.pop())
                    break
                case "*":
                    stack.push(stack.pop() * stack.pop())
                    break
                case "-":
                    let a = stack.pop()
                    let b = stack.pop()
                    stack.push(b - a)
                    break
                case "/":
                    let c = stack.pop()
                    let d = stack.pop()
                    stack.push(Math.trunc(d / c))
                    break
                default:
                    stack.push(+t)
                    break
            }
        }

        return stack.pop()
    }
}
