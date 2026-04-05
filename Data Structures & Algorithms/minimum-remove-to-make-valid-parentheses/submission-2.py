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
        
        diff = len(opened) - len(closed)
        res = []
        for index in reversed(stack):
            if s[index] == "(" and diff > 0:
                diff -= 1
            else:
                res.append(s[index])

        return "".join(res[::-1])

