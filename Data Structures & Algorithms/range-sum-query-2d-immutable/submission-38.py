class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        rows = len(matrix)
        cols = len(matrix[0])

        self.prefix = [
            [0 for _ in range(cols + 1)]
            for _ in range(rows + 1)
        ]

        for row in range(rows):

            for col in range(cols):

                top = self.prefix[row][col + 1]

                left = self.prefix[row + 1][col]

                corner = self.prefix[row][col]

                self.prefix[row + 1][col + 1] = (
                    top
                    + left
                    - corner
                    + matrix[row][col]
                )


    def sumRegion(
        self,
        row1: int,
        col1: int,
        row2: int,
        col2: int
    ) -> int:

        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        top_strip = self.prefix[row1 - 1][col2]

        left_strip = self.prefix[row2][col1 - 1]

        corner = self.prefix[row1 - 1][col1 - 1]

        sum_region = (
            self.prefix[row2][col2]
            - top_strip
            - left_strip
            + corner
        )

        return sum_region