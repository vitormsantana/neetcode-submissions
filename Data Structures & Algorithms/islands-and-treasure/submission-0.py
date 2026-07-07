class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        columns = len(grid[0])
        visited = set()

        q = collections.deque()
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0:
                    q.append((r, c))

        level = 1
        while q:
            for _ in range(len(q)):
                print(f'current q: {q}')
                print(f'current grid: {grid}')
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(columns) and (nr, nc) not in visited and grid[nr][nc] == 2147483647:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        grid[nr][nc] = level
            print('--')
            level += 1
        
        # return grid

        