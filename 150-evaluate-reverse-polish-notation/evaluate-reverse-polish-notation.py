class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}
        for token in tokens:
            if stack and token in operations:
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    stack.append(left+right)
                elif token == "-":
                    stack.append(left-right)
                elif token == "*":
                    stack.append(left*right)
                elif token == "/":
                    stack.append(int(left/right))
            else:
                stack.append(int(token))
        
        return stack[-1]
        