class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        visited = set()
        def bfs(r,c):
            visited.add((r,c))
            q = deque()
            q.append((r,c))
            while q:
                r, c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and grid[nr][nc] == "1":
                        visited.add((nr,nc))
                        q.append((nr,nc))
            return
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands