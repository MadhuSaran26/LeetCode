class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        gray_code = [i ^ (i >> 1) for i in range(2**n)]
        start_idx = gray_code.index(start)
        
        return gray_code[start_idx:] + gray_code[:start_idx]


