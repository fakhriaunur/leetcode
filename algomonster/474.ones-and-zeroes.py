#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

from typing import List


# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # m for 0s
        # n for 1s
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            # a := zero count
            #  b:= one count
            a = s.count("0")
            b = s.count("1")

            # i := zeros
            #  j := ones
            for i in range(m, a - 1, -1):
                for j in range(n, b - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - a][j - b] + 1)

        # for r in dp:
        #     print(r)
        return dp[m][n]


# @lc code=end
