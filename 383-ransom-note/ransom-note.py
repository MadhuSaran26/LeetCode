class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = [0] * 26
        for c in magazine:
            mag_count[ord(c)-ord('a')] += 1
        
        ran_count = mag_count[:]
        for c in ransomNote:
            idx = ord(c)-ord('a')
            if ran_count[idx] > 0:
                ran_count[idx] -= 1
            else:
                return False
        
        return True

        