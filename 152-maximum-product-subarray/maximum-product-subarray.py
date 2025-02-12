class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = max_so_far = min_so_far = nums[0]

        for idx in range(1, len(nums)):
            # if negative, max_so_far becomes min and min_so_far becomes max upon multiplication
            if nums[idx] < 0:
                min_so_far, max_so_far = max_so_far, min_so_far
            
            max_so_far = max(max_so_far*nums[idx], nums[idx])
            min_so_far = min(min_so_far*nums[idx], nums[idx])
            global_max = max(global_max, max_so_far)

        return global_max

        