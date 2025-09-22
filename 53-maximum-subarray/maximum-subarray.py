class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum = nums[0]
        local_sum = 0
        for num in nums:
            local_sum = max(local_sum + num, num)
            if local_sum > global_sum:
                global_sum = local_sum
        return global_sum

        