class Solution:
    def justifyText(self, current, curr_len, no_words):
        extra_space = self.max_width - curr_len
        if extra_space > 0 and no_words > 1:
            additional_spaces = extra_space // (no_words-1)
            left_spaces = extra_space % (no_words-1)
            for i in range(len(current)-1):
                current[i] += " " * additional_spaces
                if left_spaces > 0:
                    current[i] += " "
                    left_spaces -= 1
        elif no_words == 1:
            current[0] += " " * extra_space
            curr_len += extra_space
        return current

    def concatenateWord(self, word, current, curr_len, no_words):
        length = len(word)
        if curr_len + no_words-1 + length + 1 <= self.max_width:
            current.append(word)
            curr_len += length
            no_words += 1
        else:
            curr_len += no_words-1
            current = self.justifyText(current, curr_len, no_words)
            self.result.append(" ".join(current))
            current = [word]
            curr_len = length
            no_words = 1
        return current, curr_len, no_words

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        self.max_width = maxWidth
        self.result = []
        current = []
        curr_len = 0
        no_words = 0

        for word in words:
            current, curr_len, no_words = self.concatenateWord(word, current, curr_len, no_words)
        
        # add additional spaces at the end in the last line
        curr_len += no_words - 1
        extra_spaces = self.max_width - curr_len
        current[-1] += " " * extra_spaces
        self.result.append(" ".join(current))
        return self.result