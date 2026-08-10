class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counts = Counter(s1)
        current = {}
        for i in range(len(s1)):
            current[s2[i]] = current.get(s2[i], 0) + 1
        
        if current == counts:
            return True
        i = 0
        n = len(s1) - 1
        m = len(s2) - 1
        

        while n < m:
            current[s2[i]] -= 1
            if current[s2[i]] == 0:
                del current[s2[i]]

            i += 1
            n += 1
            current[s2[n]] = current.get(s2[n], 0) + 1
            if current == counts:
                return True
        
        return False
       

      
