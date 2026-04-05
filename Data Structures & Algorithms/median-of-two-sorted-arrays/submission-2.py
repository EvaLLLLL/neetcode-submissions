class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        p1, p2 = 0, 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1
        
        if p1 < len(nums1):
            merged = merged + nums1[p1:]
        if p2 < len(nums2):
            merged = merged + nums2[p2:]

        n = len(merged)

        if n % 2:
            return merged[(n - 1) // 2]
        else:
            a = merged[n // 2]
            b = merged[n // 2 - 1]
            return (a + b) / 2
