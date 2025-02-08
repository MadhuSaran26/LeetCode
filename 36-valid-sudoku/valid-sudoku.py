class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]
        result = True
        for i in range(9):
            for j in range(9):
                # element considered for check
                elem = board[i][j]
                # check the row
                if elem in row_set[i]:
                    if elem != ".":
                        result = False
                        break
                    else:
                        continue
                row_set[i].add(elem)
                # check the column
                if elem in col_set[j]:
                    if elem != ".":
                        result = False
                        break
                    else:
                        continue
                col_set[j].add(elem)
                # check the box
                box_r = i//3
                box_c = j//3
                box_id = box_r*3 + box_c
                if elem in box_set[box_id]:
                    if elem != ".":
                        result = False
                        break
                    else:
                        continue
                box_set[box_id].add(elem)
            
        return result



        