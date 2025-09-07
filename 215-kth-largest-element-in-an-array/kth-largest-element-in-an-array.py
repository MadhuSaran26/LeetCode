class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_num = min(nums)
        max_num = max(nums)
        count = [0]*(max_num - min_num + 1)
        for num in nums:
            count[num - min_num] += 1
        remain = k
        for idx in range(len(count)-1, -1, -1):
            remain -= count[idx]
            if remain <= 0:
                return idx + min_num
        return -1
        