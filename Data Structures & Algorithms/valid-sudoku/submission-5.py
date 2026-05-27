class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)


        for i in range(9):
            for j in range(9):
                
                if board[i][j] == '.':
                    pass
                elif board[i][j] not in columns[j]:
                    print(f"board[{j}][{i}]: {board[i][j]} NOT in column {j}: {columns[j]}")
                    columns[j].add(board[i][j])
                elif board[i][j] in columns[j]:
                    print(f"board[{j}][{i}]: {board[i][j]} in column {j}: {columns[j]}")
                    return False

                if board[i][j] == '.':
                    pass
                elif board[i][j] not in rows[i]:
                    rows[i].add(board[i][j])
                elif board[i][j] in rows[i]:
                    return False


                if board[i][j] == '.':
                    pass
                elif board[i][j] not in boxes[(i//3, j//3)]:
                    boxes[(i//3, j//3)].add(board[i][j])
                elif board[i][j] in boxes[(i//3, j//3)]:
                    return False


        print(columns[3])
        return True


                