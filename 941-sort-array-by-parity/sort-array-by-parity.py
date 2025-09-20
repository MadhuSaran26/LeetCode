class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nextEvenAt = 0
        for i in range(len(nums)):
            if nums[i]^1 == nums[i]+1:
                nums[i], nums[nextEvenAt] = nums[nextEvenAt], nums[i]
                nextEvenAt += 1
        return nums