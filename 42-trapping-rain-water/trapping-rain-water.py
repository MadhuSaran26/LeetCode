class Solution:
    def trap(self, height: List[int]) -> int:
        max_water = 0
        n = len(height)
        left, right = 0, n-1
        left_max, right_max = height[left], height[right]

        while left < right:
            if left_max < right_max:
                left += 1
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    max_water += left_max - height[left]
            else:
                right -= 1
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    max_water += right_max - height[right]
        
        return max_water
        