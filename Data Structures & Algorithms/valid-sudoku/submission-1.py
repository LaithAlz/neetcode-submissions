class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            seen = set()
            row = board[i]
            for num in row:
                if num == '.':
                    continue
                if num not in seen: 
                    seen.add(num)
                else:
                    return False
        
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] not in seen:
                    seen.add(board[j][i])
                else:
                    print("s")
                    return False


        # i from 0 to 2
        # j from 0 to 2

        # i from 3 to 5
        # j from 3 to 5

        # i from 6 to 8
        # j from 6 to 8
        for square in range(9):
            # print(square)
            seen = set()
            for i in range(3):
                for j in range(3):
                    # board[i][j]
                    row = (square // 3) * 3 + i
                    column = (square % 3) * 3 + j
                    num = board[row][column]
                    print("row ", row)
                    print("column", column)
                    print(num)
                    if num == '.':
                        continue
                    if num not in seen:
                        seen.add(num)
                    else:
                        print("here")
                        return False
    
        return True
                     


                    


