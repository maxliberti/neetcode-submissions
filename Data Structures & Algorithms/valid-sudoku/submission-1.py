class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(board):
            for i in range(9):
                seen = set()
                for j in range(9):
                    row_num = board[i][j]
                    if row_num.isalnum() and row_num in seen:
                        return False
                    else:
                        seen.add(row_num)
            return True
        
        def checkColumn(board):
            for i in range(9):
                seen = set()
                for j in range(9):
                    col_num = board[j][i]
                    if col_num.isalnum() and col_num in seen:
                        return False
                    else:
                        seen.add(col_num)
            return True

        def checkBox(board):
            for square in range(9):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        row = (square//3) * 3 + i
                        col = (square % 3) * 3 + j
                        square_num = board[row][col]
                        if square_num.isalnum() and square_num in seen:
                            return False
                        else:
                            seen.add(square_num)
            return True

        return checkBox(board) and checkRow(board) and checkColumn(board)


