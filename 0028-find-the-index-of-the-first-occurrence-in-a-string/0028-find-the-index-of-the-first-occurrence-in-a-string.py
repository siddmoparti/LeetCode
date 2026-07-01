class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = []
        n = len(needle)
        i = 0
        while i < len(haystack):
            string = haystack[i: i + len(needle)]
            if string == needle:
                return i
            else:
                i += 1
            
                
        

        return -1
         
    
        