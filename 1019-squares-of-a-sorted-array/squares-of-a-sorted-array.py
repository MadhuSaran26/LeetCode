class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) -1
        squares = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                squares.append(nums[left] ** 2)
                left += 1
            else:
                squares.append(nums[right] ** 2)
                right -= 1
        return squares[::-1]
        