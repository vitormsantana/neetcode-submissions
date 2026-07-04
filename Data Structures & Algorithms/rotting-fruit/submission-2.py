class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows, columns = len(grid), len(grid[0])
        visited = set()
        self.max_level = 0

        q = collections.deque()
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        time = 0
        while q:
            size = len(q)
            for _ in range(size):
                row, col = q.popleft()

                for rd, cd in directions:
                    nr, nc = row + rd, col + cd 
                    if (nr in range(rows) and nc in range(columns) and grid[nr][nc] == 1):
                        q.append((nr, nc))
                        grid[nr][nc] = 2
            if len(q) > 0:
                time += 1

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    return -1
        return time