class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        cols = len(rooms[0])
        INF = 2147483647
        

        def bfs(r,c):
            q = collections.deque()
            visited = set()
            visited.add((r,c))
            q.append((r,c))
            dir = [[0,1], [1,0], [-1,0], [0,-1]]
            level = 0

            
            while q:
                level += 1
                for i in range(len(q)):
                    r,c = q.popleft()
                    for dr,dc in dir:
                        nr = dr + r
                        nc = dc + c
                        if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and rooms[nr][nc] == INF:
                            rooms[nr][nc] = level
                            visited.add((nr,nc))
                            q.append((nr,nc))
                        elif nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and rooms[nr][nc] > 0:
                            rooms[nr][nc] = min(rooms[nr][nc], level)
                            visited.add((nr,nc))
                            q.append((nr,nc))
                            
                        

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    bfs(r,c)