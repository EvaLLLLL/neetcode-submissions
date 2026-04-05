class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        index = 0
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] < x:
                index = mid
                l = mid + 1
            else:
                r = mid - 1

        l, r = index, index
        if index + 1 < len(arr) and abs(arr[index + 1] - x) < abs(arr[index] - x):
            l, r = index + 1, index + 1

        while r - l + 1 < k:
            if l <= 0:
                r += 1
            elif r >= len(arr) - 1:
                l -= 1
            elif abs(arr[l-1] - x) <= abs(arr[r+1] - x):
                l -= 1
            else:
                r += 1

        return arr[l:r+1]
