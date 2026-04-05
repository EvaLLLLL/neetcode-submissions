class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1, p2 = 0, 0
        merged = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] > nums2[p2]:
                merged.append(nums2[p2])
                p2 += 1
            else:
                merged.append(nums1[p1])
                p1 += 1
        while p1 < len(nums1):
            merged.append(nums1[p1])
            p1 += 1
        while p2 < len(nums2):
            merged.append(nums2[p2])
            p2 += 1

        n = len(merged)
        if n % 2 == 0:
            idx1 = n // 2
            idx2 = n // 2 - 1
            return (merged[idx1] + merged[idx2]) / 2
        else:
            idx = n // 2
            return merged[idx]