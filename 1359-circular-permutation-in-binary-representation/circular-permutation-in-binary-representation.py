class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # (i>>1) equivalent to diving i by 2^1, right shift is division
        # (1<<n) equivalent to multiplying 1 by 2^n, left shoft is multiplication
        gray_code = [i ^ (i >> 1) for i in range(1<<n)]
        start_idx = gray_code.index(start)
        
        return gray_code[start_idx:] + gray_code[:start_idx]


