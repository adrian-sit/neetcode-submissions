class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        def addCell(r, c):
            nonlocal fresh
            if (min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] != 1
            ):
                return
            grid[r][c] = 2
            q.append([r, c])
            fresh -= 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1

        minute = 0
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    addCell(r + dr, c + dc)
            minute += 1
        return minute if fresh == 0 else -1