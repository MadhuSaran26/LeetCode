class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        p_len = 10 # pattern length
        if len(s) < 10:
            return []
        seen = set()
        result = set()
        
        for idx in range(len(s)-p_len+1):
            pattern = s[idx:idx+p_len]
            if pattern in seen:
                result.add(s[idx:idx+p_len])
            seen.add(pattern)
        
        return list(result)



            
        