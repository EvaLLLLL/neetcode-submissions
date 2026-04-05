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
        
        extra = []
        while len(opened) > len(closed):
            extra.append(opened.pop())

        res = []
        for index in stack:
            if index not in extra:
                res.append(s[index])

        return "".join(res)

