class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [-1]
        max_area = float("-inf")
        for idx in range(n):
            while len(stack)!=1 and heights[stack[-1]] >= heights[idx]:
                height = heights[stack.pop()]
                width = idx - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(idx)
        
        while stack[-1]!=-1:
            height = heights[stack.pop()]
            width = n - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area





        