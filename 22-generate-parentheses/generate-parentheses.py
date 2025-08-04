class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, left, right):
            if n == right and left == right:
                result.append("".join(current))
            
            if left < n:
                current.append("(")
                backtrack(current, left+1, right)
                current.pop()
            if right < left:
                current.append(")")
                backtrack(current, left, right+1)
                current.pop()
        
        backtrack([], 0, 0)
        return result



        