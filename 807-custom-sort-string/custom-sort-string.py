class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = [0]*26
        for c in s:
            count[ord(c)-ord('a')] += 1

        result = ''
        for c in order:
            result += c * count[ord(c)-ord('a')]
            count[ord(c)-ord('a')] = 0
        
        for i, cnt in enumerate(count):
            result += chr(i + 97) * cnt
        
        return result
