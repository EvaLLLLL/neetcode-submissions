class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, arr: List[int], l: int, r: int):
        if l >= r:
            return
        m = (l + r) // 2
        self.mergeSort(arr, l, m)
        self.mergeSort(arr, m + 1, r)
        self.merge(arr, l, m, r)
    
    def merge(self, arr: List[int], L: int, M: int, R: int):
        left, right = arr[L:M+1], arr[M+1:R+1]
        i, j, k = L, 0, 0

        while j < len(left) and k < len(right):
            if left[j] <= right[k]:
                arr[i] = left[j]
                j += 1
            else:
                arr[i] = right[k]
                k += 1
            i += 1
        
        while j < len(left):
            arr[i] = left[j]
            j += 1
            i += 1

        while k < len(right):
            arr[i] = right[k]
            k += 1
            i += 1