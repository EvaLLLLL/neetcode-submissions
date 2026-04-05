class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        opened = []
        closed = []

        for i in range(len(s)):
            if s[i] == ")" and len(opened) <= len(closed):
                continue
            
            if s[i] == "(":
                opened.append(i)
            if s[i] == ")":
                closed.append(i)

            stack.append(i)
        
        while len(opened) > len(closed):
            openI = opened.pop()
            stack = [i for i in stack if i != openI]

        res = [s[i] for i in stack]
        return "".join(res)

