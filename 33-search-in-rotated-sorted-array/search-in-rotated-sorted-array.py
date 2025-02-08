class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            middle = (left + right)//2
            if nums[middle] > nums[-1]:
                left = middle + 1 # pivot must be in second half
            else:
                right = middle - 1
        
        pivot = left

        def binarySearch(left, right):
            while left <= right:
                middle = (left + right)//2
                if nums[middle] == target:
                    return middle
                elif target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            
            return -1
        
        result = binarySearch(0, pivot-1)
        if result != -1:
            return result
        
        return binarySearch(pivot, len(nums)-1)