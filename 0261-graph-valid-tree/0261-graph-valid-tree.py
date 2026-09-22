class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if n - 1 != len(edges):
            return False

        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True
        
        for i in range(n):
            if i not in visited:
                if not dfs(i, -1):
                    return False
                       
        
        return len(visited) == n
        

        