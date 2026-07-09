class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        columns = len(board[0])
        visited = set()
        
        def dfs(r, c):
            if (r, c) in visited:
                return
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            board[r][c] = "#"
            while q:
                for _ in range(len(q)):
                    r, c = q.pop()
                    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr in range(rows) and nc in range(columns) and board[nr][nc] == "O" and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            q.append((nr, nc))
                            board[nr][nc] = '#'
        for r in range(rows):
            for c in range(columns):
                if (r == 0 or r == rows - 1 or c == 0 or c == columns - 1) and board[r][c] == "O":
                    dfs(r, c)
        
        for r in range(rows):
            for c in range(columns):
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"