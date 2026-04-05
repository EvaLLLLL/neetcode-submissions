class FirstUnique:

    def __init__(self, nums: List[int]):
        self.unique = {} # { value: T/F }
        self.queue = deque()
        for x in nums:
            self.add(x)

    def showFirstUnique(self) -> int:
        if not self.unique:
            return -1

        while self.queue and self.unique[self.queue[0]] == False:
            self.queue.popleft()
        
        if self.queue:
            return self.queue[0]
        
        return -1

        

    def add(self, value: int) -> None:
        if value not in self.unique:
            self.unique[value] = True
        else:
            self.unique[value] = False
        self.queue.append(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
