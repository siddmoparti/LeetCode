class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        open = 0
        closed = 0
        res = []
        self.options = ['(', ')']
        def dfs(open, closed, cur):
            if open > n:
                return
            if closed > n:
                return
            if open == n and closed == n:
                res.append("".join(cur))
                return
            if closed > open:
                return
            
            for c in self.options:
                cur.append(c)
                if c == '(':
                    dfs(open + 1, closed, cur)
                else:
                    dfs(open, closed + 1, cur)
                cur.pop()

        dfs(0,0, [])
        return res
        
        