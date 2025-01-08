#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#

from typing import List


# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])

        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]

        dp[m][n - 1] = 1
        dp[m - 1][n] = 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                downwards = dp[r + 1][c]
                rightwards = dp[r][c + 1]
                less_risky_path = min(downwards, rightwards)
                dp[r][c] = max(1, less_risky_path - dungeon[r][c])

        # print(dp)
        return int(dp[0][0])


# @lc code=end
