class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(board), len(board[0])
        wordlen = len(word)

        def dfs(r, c, index, wordlen):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or board[r][c] != word[index] or (r, c) in visit
            ):
                return False
            if index == wordlen - 1:
                return True
            visit.add((r, c))
            index += 1
            flag = False
            for dr, dc in directions:
                if not flag:
                    flag = dfs(r + dr, c + dc, index, wordlen)
            visit.remove((r, c))
            return flag 
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    visit.clear()
                    if dfs(r, c, 0, wordlen):
                        return True

        return False
        
