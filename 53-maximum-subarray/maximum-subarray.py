class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum = float('-inf')
        local_sum = 0
        for num in nums:
            local_sum = max(local_sum + num, num)
            global_sum = max(global_sum, local_sum)
        return global_sum

        