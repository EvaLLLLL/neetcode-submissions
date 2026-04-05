class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        output = []
        subset = []

        def backtrack(i):
            if len(subset) == len(digits):
                output.append("".join(subset))
                return

            for c in chars[digits[i]]:
                subset.append(c)
                backtrack(i + 1)
                subset.pop()
        
        backtrack(0)
        return output