class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n):
            if n == par[n]:
                return par[n]
            par[n] = find(par[n])
            return par[n]
            
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += p2
            else:
                par[p1] = p2
                rank[p2] += p1
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return False
        return len(edges) == n - 1
        
        