class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                # element considered for check
                elem = board[i][j]
                # ignore empty cells
                if elem == ".":
                    continue
                # check the row
                if elem in row_set[i]:
                    return False
                row_set[i].add(elem)
                # check the column
                if elem in col_set[j]:
                    return False
                col_set[j].add(elem)
                # check the box
                box_id = (i//3)*3 + (j//3) # box_r = i//3; box_c = j//3
                if elem in box_set[box_id]:
                    return False
                box_set[box_id].add(elem)
            
        return True



        