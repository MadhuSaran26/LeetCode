class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0

        count = [0]*26
        for c in chars:
            count[ord(c) - ord('a')] += 1
        
        for word in words:
            word_count = [0]*26
            for c in word:
                word_count[ord(c) - ord('a')] += 1
            
            good = True
            for i in range(26):
                if count[i] < word_count[i]:
                    good = False
                    break
            
            if good:
                result += len(word)
    
        return result