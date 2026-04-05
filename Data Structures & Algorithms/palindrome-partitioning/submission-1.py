class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        subset = []
        
        def dfs(i):
            if i >= len(s):
                res.append(subset[:])
                return

            for j in range(i, len(s)):
                word = s[i:j+1]
                if self.isPalindrome(word):
                    subset.append(word)
                    dfs(j + 1)
                    subset.pop()
        
        dfs(0)
        return res

    def isPalindrome(self, word):
        l, r = 0, len(word) - 1
        while l <= r:
            if word[l] == word[r]:
                l += 1
                r -= 1
            else:
                return False
        return True