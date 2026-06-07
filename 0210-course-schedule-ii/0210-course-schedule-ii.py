class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = [[] for i in range(numCourses)]
        for crs,pre in prerequisites:
            adj[crs].append(pre)
        visited = set()

        def dfs(crs):
            if crs in visited:
                return []
            if crs in res:
                return
            if not adj[crs]:
                res.append(crs)
                return

            visited.add(crs)

            for pre in adj[crs]:
                if dfs(pre) == []:
                    return []
            
            visited.remove(crs)
            adj[crs] = []
            res.append(crs)
            return
        

        for i in range(numCourses):
            if dfs(i) == []:
                return []
        
        return res

        