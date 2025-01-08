#
# @lc app=leetcode id=1277 lang=python3
#
# [1277] Count Square Submatrices with All Ones
#

from typing import List


# @lc code=start
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        ans = 0

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[r][c] = matrix[r][c]

                elif matrix[r][c] == 1:
                    prev_top = dp[r - 1][c]
                    prev_left = dp[r][c - 1]
                    prev_diag = dp[r - 1][c - 1]
                    dp[r][c] = min(prev_top, prev_left, prev_diag) + 1

                ans += dp[r][c]

        # print(dp)
        return ans


# @lc code=end
