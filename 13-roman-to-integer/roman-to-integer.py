class Solution:
    def romanToInt(self, s: str) -> int:
        map_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        prev_value = 0
        result = 0

        for char in s:
            current_value = map_dict[char]
            if current_value > prev_value:
                result += current_value - 2*prev_value
            else:
                result += current_value
            prev_value = current_value
        
        return result
            

        