class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Using exact variable names and approach from your snippet
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0
        
        self.prefix_buckets = [[] for bucket in range(self.rows)]

        # Build row-wise prefix sums
        for i in range(self.rows):
            prefix = 0
            for j in range(self.cols):
                prefix += matrix[i][j]
                self.prefix_buckets[i].append(prefix)

    def sumRegion(self, row_s: int, col_s: int, row_e: int, col_e: int) -> int:
        sum_region = 0

        # Process each row inside required rectangle
        for i in range(row_s, row_e + 1):
            # If rectangle starts from first column
            if col_s == 0:
                row_sum = self.prefix_buckets[i][col_e]
            else:
                prefix_left = self.prefix_buckets[i][col_s - 1]
                prefix_right = self.prefix_buckets[i][col_e]
                row_sum = prefix_right - prefix_left
            
            sum_region += row_sum

        return sum_region