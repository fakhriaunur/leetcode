#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#

# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [1, 0, 0, 0]

        for i in range(n):
            temp_dp = [0] * len(dp)

            temp_dp[0] = (dp[0] + dp[1] + dp[2] + dp[3]) % MOD
            temp_dp[1] = (dp[2] + dp[3]) % MOD
            temp_dp[2] = (dp[1] + dp[3]) % MOD
            temp_dp[3] = dp[0]

            dp = temp_dp

        return dp[0]


# @lc code=end
