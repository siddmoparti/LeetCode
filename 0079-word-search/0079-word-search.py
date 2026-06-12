class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, res_index):
            if res_index == len(word):
                return True
            if r not in range(ROWS) or c not in range(COLS):
                return False

            if board[r][c] == word[res_index]:
                res_index += 1
            else:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"
            
            found = dfs(r + 1, c, res_index) or dfs(r - 1, c, res_index) or dfs(r, c + 1, res_index) or dfs(r, c - 1, res_index)

            board[r][c] = temp
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c, 0):
                    return True
        
        return False
    
            

    

        