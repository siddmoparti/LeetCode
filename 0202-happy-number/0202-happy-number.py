class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        string_num = str(n)
        cur = 0

        while True:
            cur = 0
            for i in string_num:
                cur += int(i) * int(i)
            
            if cur == 1:
                return True
            if cur in seen:
                break
            else:
                seen.add(cur)
                string_num = str(cur)
        
        return False