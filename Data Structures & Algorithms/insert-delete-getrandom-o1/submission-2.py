class RandomizedSet:

    def __init__(self):
        self.numsMap = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.numsMap:
            return False
        self.numsMap[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numsMap:
            return False
        last = self.nums[-1]
        idx = self.numsMap[val]
        self.nums[idx] = last
        self.numsMap[last] = idx
        self.nums.pop()
        del self.numsMap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()