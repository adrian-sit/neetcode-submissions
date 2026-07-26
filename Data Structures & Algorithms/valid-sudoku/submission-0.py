class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:      

        # Check row and column first
        for i in range(len(board)):
            rowcount = {}
            colcount = {}
            for j in range(len(board[i])):
                num1 = board[i][j]
                num2 = board[j][i]
                rowcount[num1] = rowcount.get(num1, 0) + 1
                colcount[num2] = colcount.get(num2, 0) + 1
                if num1 != "." and rowcount[num1] > 1:
                    return False
                if num2 != "." and colcount[num2] > 1:
                    return False

        # Check 3x3 squares
        for i in range(0,7,3):
            for j in range(0,7,3):
                squarecount = {}
                for m in range(3):
                    for n in range(3):
                        num = board[i+m][j+n]
                        squarecount[num] = squarecount.get(num, 0) + 1
                        if num != "." and squarecount[num] > 1:
                            return False

        return True