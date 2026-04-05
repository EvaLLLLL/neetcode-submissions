class FreqStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> int:
        freq = Counter(self.stack)

        max_cnt = float("-inf")
        for cnt in freq.values():
            if cnt > max_cnt:
                max_cnt = cnt

        for i in range(len(self.stack) - 1, -1, -1):
            if freq[self.stack[i]] == max_cnt:
                val = self.stack[i]
                self.stack = self.stack[:i] + self.stack[i+1:]
                return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()