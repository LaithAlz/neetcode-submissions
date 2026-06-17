class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(list)
        rows = defaultdict(list)
        squares = defaultdict(list)
        for i in range(9):
            for j in range(9):
                row_i = board[i]
                val_row_i = board[i][j]

                if val_row_i in rows[i] and val_row_i != ".":
                    return False
                else:
                    if val_row_i != ".":
                        rows[i].append(val_row_i)

                col_i = board[j][i]
                # val_col_i = board[j][i]
                if col_i in columns[i] and col_i != ".":
                    return False
                else:
                    if col_i != ".":
                        columns[i].append(col_i)

                square = (i//3 * 3, j //3 * 3)
                
                if val_row_i in squares[square] and val_row_i != ".":
                    return False
                else:
                    if val_row_i != ".":
                        squares[square].append(val_row_i)

        return True