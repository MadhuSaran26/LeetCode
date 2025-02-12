class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for idx, char in enumerate(s):
            if char == "(":
                stack.append(idx)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    s[idx] = "" #stack.append(idx)
        
        for idx in stack:
            s[idx] = ""
            
        return "".join(s)



        