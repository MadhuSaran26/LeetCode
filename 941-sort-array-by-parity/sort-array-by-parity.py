class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nextEvenAt = 0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i], nums[nextEvenAt] = nums[nextEvenAt], nums[i]
                nextEvenAt += 1
        return nums