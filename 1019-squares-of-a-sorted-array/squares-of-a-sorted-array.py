class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) -1
        squares = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                squares.append(nums[left] * nums[left])
                left += 1
            else:
                squares.append(nums[right] * nums[right])
                right -= 1
        return squares[::-1]
        