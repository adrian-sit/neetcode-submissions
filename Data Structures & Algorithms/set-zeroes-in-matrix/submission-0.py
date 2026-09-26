class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)      
        cols = len(matrix[0])
        top_row_cleared = False

        for m in range(rows):
            for n in range(cols):
                if matrix[m][n] == 0:
                    matrix[0][n] = 0
                    if m > 0:
                        matrix[m][0] = 0
                    else:
                        top_row_cleared = True
            
        for m in range(1, rows):
            for n in range(1, cols):
                if matrix[0][n] == 0 or matrix[m][0] == 0:
                    matrix[m][n] = 0

        if matrix[0][0] == 0:
            for m in range(rows):
                matrix[m][0] = 0

        if top_row_cleared:
            for n in range(cols):
                matrix[0][n] = 0

                               