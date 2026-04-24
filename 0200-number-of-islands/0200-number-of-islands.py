from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        islands = 0
        visited = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                r,c = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == '1' and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))
            


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands
        

        