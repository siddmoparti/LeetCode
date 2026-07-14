class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0
        fresh = 0
        q = collections.deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.appendleft((i,j))

        while q and fresh > 0:
            q_length = len(q)

            for i in range(q_length):
                r,c = q.pop()
                dir = [[1,0],[0,1],[0,-1], [-1,0]]
                for dr,dc in dir:
                    nr = dr + r
                    nc = dc + c
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.appendleft((nr,nc))
                        fresh -= 1
            
            minutes += 1
                
        
        if fresh == 0:
            return minutes
        elif fresh != 0:
            return -1
        
