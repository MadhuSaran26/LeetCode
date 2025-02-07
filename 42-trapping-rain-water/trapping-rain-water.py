class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height)-1
        left_max, right_max = height[0], height[len(height)-1]
        result = 0

        while left + 1 < right:
            #higher bar exists on the right
            if right_max > left_max:
                left += 1
                #if height[left] is greater, than it can't hold water
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    result += left_max - height[left]
            #higher bar exists on the left
            else:
                right -= 1
                #if height[left] is greater, than it can't hold water
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    result += right_max - height[right]
        
        return result

        



        
        