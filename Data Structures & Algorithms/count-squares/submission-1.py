class CountSquares:

    def __init__(self):
        self.counts = {}

    def add(self, point: List[int]) -> None:
        x, y = point
        self.counts[(x, y)] = self.counts.get((x, y), 0) + 1

    def count(self, point: List[int]) -> int:
        px, py = point
        ans = 0

        for (x, y), c1 in self.counts.items():
            if x == px and y == py:
                continue
            if abs(x - px) == abs(y - py):
                c2 = self.counts.get((x, py), 0)
                c3 = self.counts.get((px, y), 0)
                ans += c1 * c2 * c3
        
        return ans