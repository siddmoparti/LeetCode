class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        dir = [[0,1], [1,0], [0,-1], [-1,0]]
        rows = len(board)
        cols = len(board[0])
        visited = set()
        def dfs(index, r, c):
            if board[r][c] != word[index]:
                return False

            if index == len(word) - 1:
                return True
            visited.add((r,c))
            
            
            for dr, dc in dir:
                nr = r + dr
                nc = c + dc
                if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited:
                    if dfs(index + 1, nr, nc):
                        return True
        
            visited.remove((r,c))
            return False
            
        
        for r in range(rows):
            for c in range(cols):
                if dfs(0, r,c):
                    return True
        
        return False


                
            