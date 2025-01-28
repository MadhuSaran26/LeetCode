class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        result = set()
        
        for idx in range(len(s)-10+1):
            pattern = s[idx:idx+10]
            if pattern in seen:
                result.add(s[idx:idx+10])
            seen.add(pattern)
        
        return list(result)



            
        