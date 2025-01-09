#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#

# @lc code=start
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(1, m + 1):
            dp[r][0] = dp[r - 1][0] + ord(s1[r - 1])

        for c in range(1, n + 1):
            dp[0][c] = dp[0][c - 1] + ord(s2[c - 1])

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if s1[r - 1] == s2[c - 1]:
                    prev_diag = dp[r - 1][c - 1]
                    dp[r][c] = prev_diag
                else:
                    prev_top = dp[r - 1][c] + ord(s1[r - 1])
                    prev_left = dp[r][c - 1] + ord(s2[c - 1])
                    dp[r][c] = min(prev_top, prev_left)

        # print(dp)
        return dp[m][n]


# @lc code=end
