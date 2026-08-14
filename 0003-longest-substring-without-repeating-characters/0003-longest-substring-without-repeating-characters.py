class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicate = set()

        left = 0
        right = left
        res = 0

        while right < len(s):
            
            while s[right] in duplicate:
                duplicate.remove(s[left])
                left += 1
            duplicate.add(s[right])
            res = max(res, right - left + 1)
            right += 1
        
        return res
            

