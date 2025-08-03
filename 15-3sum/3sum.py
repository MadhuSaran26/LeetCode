class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for fptr in range(len(nums)):
            if fptr > 0 and nums[fptr] == nums[fptr-1]:
                continue
            left, right = fptr + 1, len(nums)-1
            while left < right:
                total = nums[fptr] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[fptr], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

        return result
            
