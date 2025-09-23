class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        s = s.strip()
        negative = False
        result = 0
        for i, char in enumerate(s):
            if char.isalpha() or char in {'.', ' '} or (i != 0 and char in {'+','-'}):
                break
            if i == 0:
                if char == "-":
                    negative = True
                    continue
                if char == "+":
                    continue
                if char.isdigit():
                    result += int(char)
            else:
                result = result*10 + int(char)

        if negative:
            result = -result
        if result > INT_MAX:
            result = INT_MAX
        if result < INT_MIN:
            result = INT_MIN
        return result

        