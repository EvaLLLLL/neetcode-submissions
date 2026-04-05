class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        span = 1
        q = deque()

        while self.stack and self.stack[-1] <= price:
            q.append(self.stack.pop())
            span += 1

        while q:
            self.stack.append(q.popleft())

        self.stack.append(price)
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)