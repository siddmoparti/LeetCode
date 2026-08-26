class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def dfs(cur, start):
            if start == len(s):
                res.append(cur.copy())
                return
            
            for i in range(start, len(s)):
                if isPali(start, i):
                    cur.append(s[start: i+1])
                else:
                    continue
                dfs(cur, i + 1)
                cur.pop()
            
            return
        


        def isPali(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True
        dfs([], 0)
        return res
        