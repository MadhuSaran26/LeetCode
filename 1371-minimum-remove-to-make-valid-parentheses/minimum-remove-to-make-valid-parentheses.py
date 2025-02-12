class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = ""
        stack = deque([])
        for idx in range(len(s)):
            char = s[idx]
            if char == "(":
                stack.append(idx)
            elif char == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(idx)
        
        for idx in range(len(s)):
            if stack and idx == stack[0]:
                stack.popleft()
            else:
                result += s[idx]
            
        return result



        