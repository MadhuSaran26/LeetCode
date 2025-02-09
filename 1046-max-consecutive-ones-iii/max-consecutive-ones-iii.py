class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_window = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
                while k<0:
                    if nums[left] == 0:
                        k += 1
                    left += 1
            
            max_window = max(max_window, right-left+1)
        
        return max_window