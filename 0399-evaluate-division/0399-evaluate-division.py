class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        conversions = defaultdict(list)
        res = []
        for i in range(len(values)):
            a_to_b = values[i] 
            b_to_a = 1 / a_to_b 
            a = equations[i][0]
            b = equations[i][1]
            conversions[a].append((b, a_to_b))
            conversions[b].append((a, b_to_a))
        
        for i in range(len(queries)):

            a = queries[i][0]
            b = queries[i][1]
            if a not in conversions or b not in conversions:
                res.append(-1.0)
                continue
            q = collections.deque()
            q.append((a, 1.0))
            visited = set()
            visited.add(a)
            found = False
            while q:
                src,cost = q.popleft()
                if src == b:
                    res.append(cost)
                    found = True
                    break
              
                for dest, c in conversions[src]:
                    if dest not in visited:
                        visited.add(dest)
                        q.append((dest, cost * c))
            if not found:
                res.append(-1.0)
        
        return res
                


                

                
            
