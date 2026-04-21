from collections import deque
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        visit = set()
        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                r, c = q.popleft()
                if matrix[r][c] == target:
                            return True
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visit:
                        visit.add((nr,nc))
                        q.append((nr,nc))
        
        if not bfs(0,0):
            return False
        else:
            return True

