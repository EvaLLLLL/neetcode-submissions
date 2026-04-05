class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
            
        for x in asteroids:
            while stack and stack[-1] > 0 and x < 0:
                diff = x + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    x = 0
                else:
                    x = 0
                    stack.pop()
            if x:
                stack.append(x)

        return stack
