class Solution:
    def partitionString(self, s: str) -> List[str]:
        segments = {}
        cur = []
        for i in range(len(s)):
            cur.append(s[i])
            seg = "".join(cur)
            if seg not in segments:
                segments[seg] = True
                cur = []
            
        
        res = []
        for key in segments.keys():
            res.append(key)
                
        return res


            

        