#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        dp = [1] + [0] * n

        for r in range(1, m + 1):
            for c in range(n, 0, -1):
                if s[r - 1] == t[c - 1]:
                    dp[c] += dp[c - 1]

        # print(dp)
        return dp[n]


# @lc code=end
