#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for r in range(m + 1):
            for c in range(n + 1):
                if r == 0 or c == 0:
                    dp[r][c] = 0

                elif text1[r - 1] == text2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1] + 1

                else:
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

        return dp[m][n]


# @lc code=end
