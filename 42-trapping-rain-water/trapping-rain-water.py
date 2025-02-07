class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        result = 0

        # [3, 4, 1, 2, 2, 5, 1, 0, 2]
        #calculating max values from right until that index
        right_max = [0]*n
        for idx in range(n-2, -1, -1):
            right_max[idx] = max(height[idx+1], right_max[idx+1])
        
        #calculating max values from left until that index
        left_max = [0]*n
        for idx in range(1, n):
            left_max[idx] = max(height[idx-1], left_max[idx-1])
        
        for idx in range(n):
            #calculating hold capacity
            capacity = min(left_max[idx], right_max[idx])
            result += capacity - height[idx] if capacity - height[idx] > 0 else 0
        
        return result

        



        
        