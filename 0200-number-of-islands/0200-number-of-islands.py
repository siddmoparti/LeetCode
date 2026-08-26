class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        self.islands = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            while q:
                r,c = q.popleft()
                dir = [[0,1], [1,0], [0,-1], [-1,0]]
                for dr,dc in dir:
                    nr = dr + r
                    nc = dc + c
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and grid[nr][nc] == '1':
                        visited.add((nr,nc))
                        q.append((nr,nc))
            self.islands += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    visited.add((r,c))
                    bfs(r,c)
        return self.islands
                    

        