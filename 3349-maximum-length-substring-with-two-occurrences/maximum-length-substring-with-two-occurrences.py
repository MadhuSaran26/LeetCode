class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        result = float('-inf')
        left = 0
        seen = defaultdict(int)
        for right in range(len(s)):
            while seen[s[right]]==2:
                seen[s[left]] -= 1
                left += 1
            seen[s[right]] += 1
            result = max(result, right-left+1)
        return result



        