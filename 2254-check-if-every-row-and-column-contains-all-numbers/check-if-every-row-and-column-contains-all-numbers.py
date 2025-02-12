class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        # *matrix unpacks matrix into list of lists; zip packs corresponding elements from each list -> col
        # zip(matrix, zip(*matrix)) iterates through every row and col in a matrix simultaneously
        for row, col in zip(matrix, zip(*matrix)):
            if len(set(row)) != n or len(set(col)) != n:
                return False
        
        return True
