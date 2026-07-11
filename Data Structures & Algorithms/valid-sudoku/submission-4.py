from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] not in row:
                    if board[i][j] != '.':
                        row.add(board[i][j])
                else:
                    return False

        # check cols
        for j in range(9):
            col = set()
            for i in range(9):
                if board[i][j] not in col:
                    if board[i][j] != '.':
                        col.add(board[i][j])
                else:
                    return False

        # check boxes
        box = defaultdict(list)
        for i in range(9):
            for j in range(9):
                bucket = (i // 3, j // 3)
                if board[i][j] not in box[bucket]:
                    if board[i][j] != '.':
                        box[bucket].append(board[i][j])
                    print(box)
                else:
                    return False
        return True




