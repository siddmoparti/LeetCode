class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        res = []
        visiting = set()
        completed = set()

        def dfs(crs):
            if crs in visiting:
                return False

            if crs in completed:
                return True

            visiting.add(crs)

            for pre in adj[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            completed.add(crs)
            res.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res