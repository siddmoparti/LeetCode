class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = set()
        safe = set()
        def bfs(r,c):
            if (r,c) in visited:
                return
            visited.add((r,c))

            q = collections.deque()
            q.append((r,c))
            while q:
                r,c = q.popleft()
                dir = [[0,1], [1,0], [-1,0], [0,-1]]
                for dr,dc in dir:
                    nr = dr + r
                    nc = dc + c
                    if nr in range(m) and nc in range(n) and (nr,nc) not in visited and board[nr][nc] == 'O':
                        q.append((nr,nc))
                        safe.add((nr,nc))
                        visited.add((nr,nc))

        for r in range(len(board)):
            if board[r][0] == 'O' and (r,0) not in visited:
                safe.add((r,0))
                bfs(r, 0)
        for c in range(len(board[0])):
            if board[0][c] == 'O' and (0,c) not in visited:  
                safe.add((0,c))
                bfs(0, c)
        for c in range(len(board[0])):
            if board[m - 1][c] == 'O' and (m-1,c) not in visited:
                safe.add((m-1,c))
                bfs(m - 1, c)
        
        for r in range(len(board)):
            if board[r][ n - 1] == 'O' and (r, n -1) not in visited:
                safe.add((r,n-1))
                bfs(r, n - 1)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r,c) not in safe:
                    board[r][c] = 'X'
        

        
        