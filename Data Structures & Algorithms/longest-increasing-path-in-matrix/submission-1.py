class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        rows = len(matrix)
        columns = len(matrix[0])
        visited = {}

        def dfs(i, j):
            if (i, j) in visited:
                return visited[(i, j)]

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            r, c = i, j
            best_answer = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(columns) and matrix[nr][nc] > matrix[r][c]:
                    best_answer = max(best_answer, 1 + dfs(nr, nc))
            visited[(i, j)] = best_answer
            return visited[(i, j)]
        
        answer = 0
        for i in range(rows):
            for j in range(columns):
                answer = max(answer, dfs(i, j))
        return answer