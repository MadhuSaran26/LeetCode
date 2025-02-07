class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        result = 0

        # [3, 4, 1, 2, 2, 5, 1, 0, 2]
        #calculating max values from right until that index
        right_max = [0]*n
        right_max[n-1] = height[n-1]
        for idx in range(n-2, -1, -1):
            right_max[idx] = max(height[idx], right_max[idx+1])
        
        #calculating max values from left until that index
        left_max = [0]*n
        left_max[0] = height[0]
        for idx in range(1, n):
            left_max[idx] = max(height[idx], left_max[idx-1])
        
        for idx in range(n):
            #calculating hold capacity
            result += min(left_max[idx], right_max[idx]) - height[idx]
        
        return result

        



        
        