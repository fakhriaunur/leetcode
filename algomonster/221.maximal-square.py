#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

from typing import List


# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        max_side_length = 0

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "1":
                    prev_top = dp[r][c + 1]
                    prev_left = dp[r + 1][c]
                    prev_diag = dp[r][c]
                    dp[r + 1][c + 1] = min(prev_top, prev_left, prev_diag) + 1

                max_side_length = max(max_side_length, dp[r + 1][c + 1])

        # print(dp)
        return max_side_length**2


# @lc code=end
