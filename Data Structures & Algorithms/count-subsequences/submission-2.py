class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        visited = {}
        def dfs(i, j):
            if (i, j) in visited:
                return visited[(i, j)]

            if j >= len(t):
                visited[(i, j)] = 1
                return 1

            if i >= len(s):
                visited[(i, j)] = 0
                return 0
            
            if s[i] == t[j]:
                visited[(i, j)] = dfs(i + 1, j) + dfs(i+1, j + 1)
                return visited[(i, j)]
            visited[(i, j)] = dfs(i + 1, j)
            return visited[(i, j)]
    
        return dfs(0, 0)    