class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for col in row:
                if col == ".":
                    continue
                if col in seen:
                    return False
                seen.add(col)    

        for i in range(9):
            seen = set()
            for j in range(9): 
                if board[j][i] == ".":
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])


        for i in range(0,9,3):
            for j in range(0,9,3):
                seen = set()
                for n in range(i,i+3):
                    for f in range(j,j+3):
                        if board[n][f] == ".":
                            continue
                        if board[n][f] in seen:
                            return False
                        seen.add(board[n][f])    
        return True                
                        




        

        