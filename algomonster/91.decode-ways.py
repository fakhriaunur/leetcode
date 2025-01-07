#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] + [0] * n

        if s[0] != "0":
            dp[1] = 1

        for i in range(2, n + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]

            if s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] <= "6"):
                dp[i] += dp[i - 2]

        return dp[n]


# @lc code=end
