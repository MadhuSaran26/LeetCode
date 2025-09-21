class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = len(nums) - 2
        l = len(nums) - 1
        
        # iterate till the index where it is non-decreasing
        while k >= 0 and nums[k] >= nums[k+1]:
            k -= 1
        
        if k == -1:
            nums.reverse()
            return
        
        # iterate till the index of the number that is greater than nums[k]
        while l >= 0 and nums[k] >= nums[l]:
            l -= 1
        
        # swap nums[k] and nums[l] to form the next permutation in the lexographical order
        nums[k], nums[l] = nums[l], nums[k]

        # swap only the part after the new nums[k]
        nums[k+1:] = nums[k+1:][::-1]

        