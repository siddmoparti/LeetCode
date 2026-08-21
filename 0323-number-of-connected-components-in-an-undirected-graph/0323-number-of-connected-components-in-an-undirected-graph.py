class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 0:1
        # 1:0,2
        # 2:1,3
        # 3:2,4
        # 4:3

        components = 0
        visited = set()
        adj = { i:[] for i in range(n)}
        for parent,child in edges:
            adj[parent].append(child)
            adj[child].append(parent)
        
        def dfs(node):
            visited.add(node)
        
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            return

        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        
        return components
        



