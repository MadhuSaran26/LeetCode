class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for idx in range(len(s)):
            char = s[idx]
            if char == "(":
                stack.append(idx)
            elif char == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(idx)
        
        for idx in stack:
            s[idx] = ""
            
        return "".join(s)



        