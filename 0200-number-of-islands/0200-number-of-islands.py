class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        visited = set()
        q = collections.deque()
        
        def bfs(r,c):
            while q:
                r,c = q.pop()
                dir = [[0,1], [1,0], [-1,0], [0,-1]]
                for dr,dc in dir:
                    nr = dr + r
                    nc = dc + c
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == "1" and (nr,nc) not in visited:
                        q.appendleft((nr,nc))
                        visited.add((nr,nc))         
            return
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i,j) not in visited:
                    q.appendleft((i,j))
                    visited.add((i,j))
                    bfs(i,j)
                    islands += 1

        return islands
        
        