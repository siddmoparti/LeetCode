class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i,eq in enumerate(equations):
            a,b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q, visit = deque(), set()
            q.append([src,1])
            visit.add(src)
            while q:
                node, weight = q.popleft()
                if node == target:
                    return weight
                for nei, new_weight in adj[node]:
                    if nei not in visit:
                        q.append([nei, new_weight * weight])
                        visit.add(nei)
            return -1
        
        res = []
        for q in queries:
            res.append(bfs(q[0], q[1]))
        
        return res

        # return [bfs(q[0], q[1]) for q in queries]
