class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.max_area = 0
        visited = set()

        def bfs(r,c):
            if (r,c) in visited:
                return
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            cur_area = 0
            dir = [[0,1], [1,0], [0,-1], [-1,0]]
            while q:
                cur_area += 1
                r,c = q.popleft()
                for dr,dc in dir:
                    nr = dr + r
                    nc = dc + c
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and grid[nr][nc] == 1:
                        visited.add((nr,nc))
                        q.append((nr,nc))

            self.max_area = max(self.max_area, cur_area)
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    bfs(r,c)
        
        return self.max_area
        