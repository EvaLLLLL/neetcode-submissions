class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # A: [3, 4,| 5, 6, 7]
        # B: [2, 3, 4,| 5, 6, 7]

        # [1,| 3]
        # [2,| 4]

        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) # choose number of A
        while l <= r:
            numA = (l + r) // 2
            numB = half - numA

            ALeft = A[numA - 1] if numA - 1 >= 0 else float("-inf")
            ARight = A[numA] if numA < len(A) else float("inf")

            BLeft = B[numB - 1] if numB - 1 >= 0 else float("-inf")
            BRight = B[numB] if numB < len(B) else float("inf")


            if ALeft <= BRight and BLeft <= ARight:
                if total % 2:
                    return min(ARight, BRight)
                else:
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            elif ALeft > BRight:
                r = numA - 1
            else:
                l = numA + 1
        

        