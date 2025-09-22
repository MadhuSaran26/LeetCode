class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        p1, p2 = n1-1, n2-1
        carry = 0
        result = ""
        while p1 >= 0 or p2 >= 0 or carry:
            csum = carry
            if p1 >= 0:
                csum += int(num1[p1])
                p1 -= 1
            if p2 >= 0:
                csum += int(num2[p2])
                p2 -= 1
            carry = csum // 10
            result += str(csum%10)
        return result[::-1]





        