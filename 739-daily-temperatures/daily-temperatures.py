class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = [] #to hold the temperatures for which warmer days are yet to be seen

        for curr_day in range(n):
            while stack and temperatures[stack[-1]] < temperatures[curr_day]:
                prev_day = stack.pop()
                result[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        
        return result
        