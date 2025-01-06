#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        dp[1][1] = 1

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if r == 1 and c == 1:
                    continue

                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[m][n]


# @lc code=end
