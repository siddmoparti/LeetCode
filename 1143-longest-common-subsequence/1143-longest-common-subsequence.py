class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #   a c e 
        # a 1 1 1
        # b 1 1 1
        # c 1 2 2
        # d 1 2 2
        # e 1 2 3

        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for r in range(1, len(text1) + 1):
            for c in range(1, len(text2) + 1):
                if text1[r - 1] == text2[c - 1]:
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
        
        return dp[len(text1)][len(text2)]
        