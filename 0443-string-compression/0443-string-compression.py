class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        l = 0
        r = 0

        while r < len(chars):
            cur_char = chars[r]
            while r < len(chars) and chars[l] == chars[r]: 
                r += 1
            
            chars[write] = cur_char
            write += 1

            count = r - l
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
                
            l = r
    
            
        return write
            




        