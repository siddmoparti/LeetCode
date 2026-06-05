class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        l = 0
        r = 0

        while r < len(chars):
            cur_char = chars[r]
            while r < len(chars) and chars[l] == chars[r]: 
                r += 1
            if r - l == 1:
                s += cur_char
            else:
                s += cur_char
                s += str(r - l)
            l = r
        
        
        for i in range(len(s)):
            chars[i] = s[i]
            
        return len(s)
            




        