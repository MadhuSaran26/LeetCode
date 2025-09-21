class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        width = valueDiff + 1
        bucket = dict()
        for i, num in enumerate(nums):
            n = num // width
            if n in bucket:
                return True
            if (n-1) in bucket and num - bucket[n-1] <= valueDiff:
                return True
            if (n+1) in bucket and bucket[n+1] - num <= valueDiff:
                return True
            bucket[n] = num
            if i >= indexDiff:
                del bucket[nums[i - indexDiff] // width]
        return False
        