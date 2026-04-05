class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = [0, 0] # 5, 10
        for n in bills:
            if n == 5:
                count[0] += 1
            elif n == 10:
                if count[0] >= 1:
                    count[0] -= 1
                    count[1] += 1
                else:
                    return False
            else:
                if count[1] >= 1 and count[0] >= 1:
                    count[1] -= 1
                    count[0] -= 1
                elif count[0] >= 3:
                    count[0] -= 3
                else:
                    return False
        return True
