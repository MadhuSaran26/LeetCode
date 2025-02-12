class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0

        count = [0]*26
        for c in chars:
            count[ord(c) - ord('a')] += 1
        
        good = True
        for word in words:
            word_count = count[:]
            for c in word:
                idx = ord(c) - ord('a')
                if word_count[idx] > 0:
                    word_count[idx] -= 1
                else:
                    good = False
                    break
            
            if good:
                result += len(word)
            
            good = True
    
        return result