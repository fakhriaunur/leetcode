#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

from typing import List


# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # cell values are non-negatives, safe to init all-0
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        for r in range(1, m):
            dp[r][0] = dp[r - 1][0] + grid[r][0]

        for c in range(1, n):
            dp[0][c] = dp[0][c - 1] + grid[0][c]

        for r in range(1, m):
            for c in range(1, n):
                prev_top = dp[r - 1][c]
                prev_left = dp[r][c - 1]
                dp[r][c] = min(prev_top, prev_left) + grid[r][c]

        # print(dp)
        return dp[-1][-1]


# @lc code=end
