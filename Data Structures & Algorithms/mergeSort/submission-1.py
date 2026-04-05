# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, a: List[Pair], s: int, e: int) -> List[Pair]:
        if s >= e:
            return a

        m = (s + e) // 2
        self.mergeSortHelper(a, s, m)
        self.mergeSortHelper(a, m + 1, e)
        self.merge(a, s, m, e)
        return a

    def merge(self, a: List[Pair], s: int, m: int, e: int):
        i, j = s, m + 1
        tmp = []

        while i <= m and j <= e:
            if a[i].key <= a[j].key:
                tmp.append(a[i])
                i += 1
            else:
                tmp.append(a[j])
                j += 1
        
        while i <= m:
            tmp.append(a[i])
            i += 1

        while j <= e:
            tmp.append(a[j])
            j += 1

        a[s:e+1] = tmp