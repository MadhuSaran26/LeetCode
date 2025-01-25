class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort() # sorting helps in handling duplicates in candidates

        def backtracking(current, remaining, start):
            if remaining == 0:
                result.append(list(current))
                return
            
            if remaining < 0:
                return
            
            for idx in range(start, len(candidates)):
                if idx > start and candidates[idx] == candidates[idx-1]:
                    continue
                # stop when the left out elements in candidates are higher than "remaining"
                if candidates[idx] > remaining:
                    break
                current.append(candidates[idx])
                backtracking(current, remaining - candidates[idx], idx+1)
                current.pop()
            
        
        backtracking([], target, 0)
        return result
        