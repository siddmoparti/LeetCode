class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                r, c = q.popleft()

                directions = [[1,0], [0,1], [-1,0], [0,-1]]
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited and board[nr][nc] == "O":
                        visited.add((nr, nc))
                        q.append((nr, nc))

        for r in range(rows):
            if board[r][0] == "O" and (r, 0) not in visited:
                bfs(r, 0)
            if board[r][cols - 1] == "O" and (r, cols - 1) not in visited:
                bfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == "O" and (0, c) not in visited:
                bfs(0, c)
            if board[rows - 1][c] == "O" and (rows - 1, c) not in visited:
                bfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"