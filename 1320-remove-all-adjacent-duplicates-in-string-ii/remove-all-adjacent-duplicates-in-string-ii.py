class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == (c, k-1):
                stack.pop()
            elif stack and stack[-1][0] == c and stack[-1][1] != k-1:
                stack[-1] = (c, stack[-1][1] + 1)
            else:
                stack.append((c, 1))
        result = ""
        while stack:
            c, cnt = stack.pop()
            result += c * cnt
        return result[::-1]
                

        