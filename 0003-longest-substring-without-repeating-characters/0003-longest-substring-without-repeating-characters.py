class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        visited = set()

        while r < len(s):
            
            while s[r] in visited:
                visited.remove(s[l])
                l += 1

            visited.add(s[r])
            res = max(res, r - l + 1)
            r += 1
    

        return res
