class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = { i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            prereqs[crs].append(pre)
            # prereqs[pre].append(crs)
        
        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            if not prereqs[crs]:
                return True
            
            visited.add(crs)
            for pre in prereqs[crs]:
                if not dfs(pre):
                    return False
            
            prereqs[crs] = []
            visited.remove(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

        {1:0}