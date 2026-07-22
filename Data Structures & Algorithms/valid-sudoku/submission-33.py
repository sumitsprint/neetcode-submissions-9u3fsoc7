class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            see = set()
            for col in row:
                if col == ".":
                    continue
                if col in see:
                    return False
                    
                see.add(col)

        for col in range(9):
            see = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in see:
                    return False
                see.add(board[row][col])

        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                see = set()
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in see:
                            return False
                        see.add(board[i][j])    


        return True




            

            

                    

        