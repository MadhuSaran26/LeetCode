class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        p1 = p2 = 0
        num1, num2 = num1[::-1], num2[::-1]
        carry = 0
        result = ""
        while p1 < n1 or p2 < n2 or carry:
            csum = carry
            if p1 < n1:
                csum += int(num1[p1])
                p1 += 1
            if p2 < n2:
                csum += int(num2[p2])
                p2 += 1
            carry = csum // 10
            result += str(csum%10)
        return result[::-1]





        