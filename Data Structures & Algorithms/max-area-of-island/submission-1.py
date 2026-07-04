class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        rows, columns = len(grid), len(grid[0])
        self.currSize = 0
        self.maxSize = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(columns) and grid[r][c] == 1 and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))
                        self.currSize += 1
                        self.maxSize = max(self.maxSize, self.currSize)
        
        for r in range(rows):
            for c in range(columns):
                if r in range(rows) and c in range(columns) and grid[r][c] == 1 and (r, c) not in visited:
                    self.currSize = 1
                    self.maxSize = max(self.maxSize, self.currSize)
                    bfs(r, c)
        return self.maxSize