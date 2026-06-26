class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            see= set()
            for val in row:
                if val == ".":
                    continue
                if val in see:
                    return False
                see.add(val) 

        # for cols

        for col in range(9):
            see = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in see:
                    return False
                see.add(board[row][col])

        #for box

        for i in range(0,9,3):
            for j in range(0,9,3):
                see = set()
                for l in range(i,i+3):
                    for k in range(j,j+3):
                        if board[l][k] == ".":
                            continue
                        if board[l][k] in see:
                            return False
                        see.add(board[l][k])
        return True                    
        








                   

        