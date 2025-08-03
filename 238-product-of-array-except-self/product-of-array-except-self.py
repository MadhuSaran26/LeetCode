class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_left, prefix_right = [1]*(n+1), [1]*(n+1)
        for i in range(n):
            prefix_left[i+1] = prefix_left[i] * nums[i]
        
        for j in range(n-1, -1, -1):
            prefix_right[j] = prefix_right[j+1] * nums[j]

        result = [1]*n
        for i in range(n):
            result[i] = prefix_left[i] * prefix_right[i+1]
        return result


        