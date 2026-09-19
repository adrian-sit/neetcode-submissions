class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        for i in range (COLS):
            pacific.add((0, i))
            atlantic.add((ROWS - 1, i))
        for i in range(ROWS):
            pacific.add((i, 0))
            atlantic.add((i, COLS - 1))

        def dfs(r, c, ocean):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS
            ):
                return

            if ocean == "p":
                if (r, c) not in pacific:
                    pacific.add((r, c))
            else:
                if (r, c) not in atlantic:
                    atlantic.add((r, c))
            
            for dr, dc in directions:
                if (r + dr < 0 or c + dc < 0 or r + dr >= ROWS or
                c + dc >= COLS):
                    continue
                if ocean == "p":
                    if heights[r][c] <= heights[r + dr][c + dc] and (r + dr, c + dc) not in pacific:
                        dfs(r + dr, c + dc, "p")
                else:
                    if heights[r][c] <= heights[r + dr][c + dc] and (r + dr, c + dc) not in atlantic:
                        dfs(r + dr, c + dc, "a")

            return

        for r, c in pacific.copy():
            dfs(r, c, "p")

        for r, c in atlantic.copy():
            dfs(r, c, "a")

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res