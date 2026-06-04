class Solution:

    def mutate(self, start, end):
        diff = 0
        for i in range(8):
            if start[i] != end[i]:
                diff += 1
            if diff > 1:
                return False
        return True
    #consider a diff of 0 and 1 to be true

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        visited = set()

        def bfs(sGene):
            q = deque()
            q.append([sGene, 0])
            visited.add(sGene)

            while q:
                
                g, steps = q.popleft()
                for Egene in bank:
                    if Egene not in visited and self.mutate(g, Egene):
                        if Egene == endGene:
                            return steps + 1
                        q.append([Egene, steps + 1])
                        visited.add(Egene)
                
            return -1
        
        return bfs(startGene)
                

            
        
