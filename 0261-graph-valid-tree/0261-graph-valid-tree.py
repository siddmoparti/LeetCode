class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 0:1
        # 1:0,2,3,4
        # 2:1,3
        # 3:1,2
        # 4:1

        visited = set()
        adj = { i:[] for i in range(n)}
        for parent,child in edges:
            adj[parent].append(child)
            adj[child].append(parent)
        
        def dfs(parent,child):
            
            visited.add(child)
            for new_child in adj[child]:
                if new_child == parent:
                    continue
                if new_child in visited:
                    return False
                if not dfs(child, new_child):
                    return False
            
            return True
        
        if not dfs(-1, 0):
            return False
        
        return len(visited) == n




        