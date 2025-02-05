class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtracking(current, left_cnt, right_cnt):
            if len(current)==2*n:
                result.append("".join(current))
            if left_cnt < n:
                current.append("(")
                backtracking(current, left_cnt+1, right_cnt)
                current.pop()
            if right_cnt < left_cnt:
                current.append(")")
                backtracking(current, left_cnt, right_cnt+1)
                current.pop()

        backtracking([], 0, 0)
        return result        