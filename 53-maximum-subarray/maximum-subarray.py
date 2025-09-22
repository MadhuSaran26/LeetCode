class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum = nums[0]
        local_sum = 0
        for num in nums:
            local_sum += num
            if local_sum > global_sum:
                global_sum = local_sum
            if local_sum < 0:
                local_sum = 0
        return global_sum

        