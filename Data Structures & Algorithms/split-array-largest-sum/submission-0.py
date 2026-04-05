class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        def canSplit(largest):
            subarray = 1
            curSum = 0
            for n in nums:
                if curSum + n > largest:
                    subarray += 1
                    curSum = n
                else:
                    curSum += n
            return subarray <= k

        while l <= r:
            mid = l + (r - l) // 2

            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
        