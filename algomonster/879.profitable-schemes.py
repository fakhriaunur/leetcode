#
# @lc app=leetcode id=879 lang=python3
#
# [879] Profitable Schemes
#

from typing import List


# @lc code=start
class Solution:
    def profitableSchemes(
        self, n: int, minProfit: int, group: List[int], profit: List[int]
    ) -> int:
        MOD = 10**9 + 7
        num_crimes = len(group)

        dp = [
            [[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(num_crimes + 1)
        ]

        for j in range(n + 1):
            dp[0][j][0] = 1

        for i, (members, gain) in enumerate(zip(group, profit), 1):
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    dp[i][j][k] = dp[i - 1][j][k]

                    if j >= members:
                        dp[i][j][k] += dp[i - 1][j - members][max(0, k - gain)]
                        dp[i][j][k] %= MOD

        # print(dp[num_crimes][n])
        return dp[num_crimes][n][minProfit]


# @lc code=end
