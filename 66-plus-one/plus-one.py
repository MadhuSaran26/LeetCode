class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        length = len(digits)
        for i in range(length-1, -1, -1):
            if i == length-1:
                value = digits[i] + 1
            else:
                value = carry + digits[i]
            carry = value // 10
            digits[i] = value % 10
        if carry:
            digits = [1] + digits
        return digits
        