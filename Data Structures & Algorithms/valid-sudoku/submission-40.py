class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows= len(board)
        cols = len(board[0])

        #rows
        for row in board:
            see = set()
            for col in row:
                if col == ".":
                    continue
                if col in see:
                    return False
                see.add(col)

        #cols
        for col in range(cols):
            see = set()
            for row in range(rows):
                if board[row][col] == ".":
                    continue
                if board[row][col] in see:
                    return False
                see.add(board[row][col]) 

        #boxes
        for row in range(0, rows, 3):
            for col in range(0, cols, 3):
                see = set()
                for i in range(row, row + 3):
                    for j in range(col, col+3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in see:
                            return False
                        see.add(board[i][j])
        return True                    




                









        