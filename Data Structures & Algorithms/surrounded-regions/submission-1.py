class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(board), len(board[0])
        not_surrounded = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or board[r][c] == "X" or (r, c) in not_surrounded
            ):
                return
            not_surrounded.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for i in range(COLS):
            if board[0][i] == "O":
                dfs(0, i)  
            if board[ROWS - 1][i] == "O":
                dfs(ROWS - 1, i)
        for i in range(ROWS):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][COLS - 1] == "O":
                dfs(i, COLS - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in not_surrounded:
                    board[r][c] = "X"
