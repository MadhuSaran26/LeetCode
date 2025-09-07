class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        current = 0
        operation = '+'
        stack = []
        for i, char in enumerate(s):
            if char.isdigit():
                current = current * 10 + int(char)
            if (not char.isspace() and not char.isdigit()) or i == n-1:
                if operation == '+':
                    stack.append(current)
                if operation == '-':
                    stack.append(-current)
                if operation == '*':
                    stack.append(stack.pop() * current)
                if operation == '/':
                    stack.append(int(stack.pop() / current))
                operation = char
                current = 0
        return sum(stack)

            





        