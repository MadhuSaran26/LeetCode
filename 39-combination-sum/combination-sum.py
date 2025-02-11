class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtracking(curr, remaining, start):
            if remaining == 0:
                result.append(curr[:])
                return
            
            for idx in range(start, len(candidates)):
                if remaining-candidates[idx] >= 0:
                    curr.append(candidates[idx])
                    backtracking(curr, remaining-candidates[idx], idx)
                    curr.pop()
        
        backtracking([], target, 0)
        return result