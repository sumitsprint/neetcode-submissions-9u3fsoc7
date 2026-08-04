class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in  board:
            see = set()
            for col in row:
                if col == ".":
                    continue

                if col in see:
                    return False

                see.add(col)

        for row in range(len(board[0])):
            see = set()
            for col in range(len(board)):
            
    
                if board[col][row] == ".":
                    continue

                if board[col][row] in see:
                    return False

                see.add(board[col][row])

        for box_row in range(0, len(board), 3):
           
            for box_col in range(0, len(board[0]), 3):
                 see = set()
                 for row in range(box_row, box_row+3, 1):
                    for col in range(box_col, box_col+3, 1):
                        if board[row][col] == ".":
                            continue

                        if board[row][col] in see:
                            return False
                        see.add(board[row][col])



            
    
        return True        



        
                        
        