class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for idx, char in enumerate(s):
            if char == ")":
                if not stack:
                    s[idx] = ""
                else:
                    stack.pop()
            if char == "(":
                stack.append(idx)
        while stack:
            i = stack.pop()
            s.pop(i)
        
        return "".join(s)
            





        