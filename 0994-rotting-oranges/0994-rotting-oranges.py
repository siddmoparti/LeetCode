class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        minutes = 0
        q = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))

        while q and fresh > 0:
            rotten = len(q)
            for i in range(rotten):
                dir = [[0,1], [1,0], [0,-1], [-1,0]]
                r,c = q.popleft()
                for dr,dc in dir:
                    nr = dr + r
                    nc = dc + c
                    if nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            minutes += 1
        
        if fresh == 0:
            return minutes
        else:
            return -1
        
