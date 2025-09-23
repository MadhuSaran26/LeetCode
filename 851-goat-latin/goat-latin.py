class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(" ")
        result = []
        for i, word in enumerate(words):
            if word[0].lower() in {'a', 'e', 'i', 'o', 'u'}:
                word += "ma"
            else:
                word = word[1:] + word[0] + "ma"
            word += "a" * (i+1)
            result.append(word)
        return " ".join(result)
        