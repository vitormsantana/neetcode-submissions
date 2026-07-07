class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()

        rows = len(heights)
        columns = len(heights[0])

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == 0 or c == 0:
                    pacific.add((r, c))
                
                if r == len(heights) -1 or c == len(heights[0]) - 1:
                    atlantic.add((r, c))
        
        q_pacific = collections.deque()
        for item in pacific:
            q_pacific.append(item)

        q_atlantic = collections.deque()
        for item in atlantic:
            q_atlantic.append(item)

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q_pacific:
            for _ in range(len(q_pacific)):
                r, c = q_pacific.pop()
                for dr, dc in (directions):
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(columns) and (nr, nc) not in pacific and r in range(rows) and c in range(columns) and heights[nr][nc] >= heights[r][c]:
                        q_pacific.append((nr, nc))
                        pacific.add((nr, nc))

        while q_atlantic:
            for _ in range(len(q_atlantic)):
                r, c = q_atlantic.pop()
                for dr, dc in (directions):
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(columns) and (nr, nc) not in atlantic and r in range(rows) and c in range(columns) and heights[nr][nc] >= heights[r][c]:
                        q_atlantic.append((nr, nc))
                        atlantic.add((nr, nc))

        res = []
        for item in atlantic:
            if item in pacific:
                res.append(item)
        
        return res