class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        result = 0
        stack = []
        for char in s:
            if stack and char == ")":
                stack.pop()
            elif not stack and char == ")":
                result += 1
            else:
                stack.append("(")
        result += len(stack)
        return result
            
        