class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        q = collections.deque()
        visited = set()

        def bfs(r,c):
            q = collections.deque([(r,c)])
            visited.add((r,c))
            
        
            cur_path = set()
            edge = False
            while q:
                r,c = q.popleft()
                cur_path.add((r,c))
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    edge = True
                dir = [[-1,0], [1,0], [0,-1], [0,1]]
                for dr,dc in dir:
                    nr = dr + r
                    nc = dc + c
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and board[nr][nc] == 'O':
                        q.append((nr,nc))
                        visited.add((nr,nc))
                    
            if not edge:
                for r,c in cur_path:
                    board[r][c] = 'X'         
            return
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and board[r][c] == 'O':
                    bfs(r,c)
                    

            

        