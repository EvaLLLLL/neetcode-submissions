class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ""

        for c in s:
            if c == "]":
                m = ""
                while stack and stack[-1] != "[":
                    m = stack.pop() + m

                stack.pop() # "["

                x = ""
                while stack and stack[-1].isdigit():
                    x = stack.pop() + x

                stack.append(int(x) * m)
            else:
                stack.append(c)
        
        return "".join(stack)
