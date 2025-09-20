class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = [0]*26
        for c in s:
            count[ord(c)-ord('a')] += 1

        result = ''
        order_set = set()
        for c in order:
            result += c * count[ord(c)-ord('a')]
            order_set.add(c)
        
        for c in s:
            if c not in order_set:
                result += c
        
        return result
