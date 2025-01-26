class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result = []
        if n == 1:
            return result

        def backtracking(current, remaining, start):
            if len(current)>0:
                result.append(current+[remaining])
            
            for idx in range(start, int(remaining**0.5)+1):
                if remaining % idx == 0:
                    backtracking(current+[idx], remaining//idx, idx)
        
        backtracking([], n, 2)
        return result
        