class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rows = len(matrix)
        cols = len(matrix[0])
        visited = set()
        res = []

        def dfs(r,c, dir):
            if matrix[r][c] in visited:
                return
            
            res.append(matrix[r][c])
            visited.add((r,c))
            
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            dr,dc = directions[dir]
            nr = dr + r
            nc = dc + c
            if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited:
                dfs(nr,nc, dir)
            else:
                i = 0
                while i < 4:
                    if i == dir:
                        i += 1
                        continue
                    dr,dc = directions[i]
                    nr = dr + r
                    nc = dc + c
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited:
                        dfs(nr,nc, i)
                        return
                    i += 1
                    
            return

        dfs(0,0,0)
        return res