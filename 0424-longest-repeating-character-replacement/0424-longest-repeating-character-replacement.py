
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        right = left
        res = 0
        most_freq = 0
        while right < len(s) and left <= right:
            freq[s[right]] = freq.get(s[right], 0) + 1
            most_freq = max(most_freq, freq[s[right]])

            while (right - left + 1) - most_freq > k:
                freq[s[left]] -= 1
                left += 1
            
            res = right - left + 1
            right += 1
                
        
        return res

        
           

        