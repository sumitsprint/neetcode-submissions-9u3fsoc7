class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix = [[0 for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                top = 0
                left = 0
                corner = 0
                if col > 0:
                    left = self.prefix[row][col-1]
                if row > 0:
                    top = self.prefix[row - 1][col]
                if row > 0 and col > 0:
                    corner = self.prefix[row - 1][col - 1]        
                self.prefix[row][col] = matrix[row][col] + left + top - corner

                
            

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top_strip = 0
        left_strip = 0
        corner_fix = 0
        if row1 > 0:
            top_strip = self.prefix[row1 - 1][col2]
        if col1 > 0:
            left_strip = self.prefix[row2][col1 - 1]   
        if col1>0 and row1>0:
            corner_fix = self.prefix[row1 -1][col1 -1]
        return self.prefix[row2][col2] - left_strip - top_strip + corner_fix       


        

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)