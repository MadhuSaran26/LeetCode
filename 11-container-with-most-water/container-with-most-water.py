class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_amount = 0
        while left < right:
            length = right-left
            if height[left] < height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1
            max_amount = max(max_amount, h*length)
        return max_amount

