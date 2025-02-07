class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 1
        for idx in range(1, len(nums)):
            if nums[idx-1] > nums[idx]:
                count -= 1
                if count < 0:
                    return False
                if idx < 2 or nums[idx-2] <= nums[idx]:
                    nums[idx-1] = nums[idx]
                else:
                    nums[idx] = nums[idx-1]
        return True
        