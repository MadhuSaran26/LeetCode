class Solution:
    def trap(self, height: List[int]) -> int:
        max_water = 0
        if not height:
            return max_water
            
        n = len(height)

        max_left = [0]*n
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])
        
        max_right = [0]*n
        max_right[n-1] = height[n-1]
        for j in range(n-2, -1, -1):
            max_right[j] = max(max_right[j+1], height[j])

        for k in range(n):
            max_water += min(max_left[k], max_right[k]) - height[k]
        
        return max_water
        