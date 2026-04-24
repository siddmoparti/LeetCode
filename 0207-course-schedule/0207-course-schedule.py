class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqs = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preReqs[crs].append(pre)
        
        visited = set()

        def dfs(crs):
            if not preReqs[crs]:
                return True
            if crs in visited:
                return False
            
            visited.add(crs)
            for pre in preReqs[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            preReqs[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
